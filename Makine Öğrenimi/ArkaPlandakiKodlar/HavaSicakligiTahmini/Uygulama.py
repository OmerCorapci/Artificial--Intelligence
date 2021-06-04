veri = {}
from tkinter import *
import tkinter as tk  
from veriCekme import*

import numpy as np
import tensorflow as tf
from tensorflow import keras

def secim(deneme):
    
    sehir = clicked.get()
    ist = bilgi(sehir)
    m_id = ist["merkezId"]
    veriler = merkez(m_id)
    
    sicaklikk.configure(text=veriler["Sicaklik"])
    if veriler["Yagis"] == -9999:
        veriler["Yagis"] = 0
        
    yagiss.configure(text=veriler["Yagis"] )
    ruzgar_yonuu.configure(text=veriler["RuzgarYonu"])
    ruzgarr.configure(text=veriler["Ruzgar_Hizi"])
    nemm.configure(text=veriler["Nem"])
    abasincc.configure(text=veriler["AktuelBasinc"])
    dibasinckk.configure(text=veriler["DenizeBasinc"])
    durumm.configure(text=veriler["SuAnkiHavaDurumu"])
    
def Tahmin():
    
    sehir = clicked.get()
    ist = bilgi(sehir)
    m_id = ist["merkezId"]
    veriler = merkez(m_id)
    
    if veriler["Yagis"] == -9999:
        veriler["Yagis"] = 0
        
    array = np.array([veriler["Sicaklik"],
                          veriler["Nem"],
                          veriler["Ruzgar_Hizi"],
                          veriler["RuzgarYonu"],
                          veriler["Yagis"] ]).reshape(1,5)
                      
    model = keras.models.load_model('model')
    sonuc = model.predict(array)[0][0]
    tahminn.configure(text = sonuc)
    
    
root = tk.Tk()  
root.geometry('400x400+100+200')  
root.title('Hava Durumu Tahmini')  
   

Sehirler= [
    "Rize",
    "İstanbul",
    "Ankara"]

clicked = StringVar()
clicked.set(Sehirler[1])

Veriler = tk.Label(root, text="Veriler    ").grid(row=0, column=1) 

sicaklik = tk.Label(root, text="Sıcaklık").grid(row=1, column=0)
sicaklikk = tk.Label(root, text=veri["Sicaklik"])
sicaklikk.grid(row=1, column=1) 

yagis = tk.Label(root, text="Yağış(mm)").grid(row=2, column=0)
if veri["Yagis"] == -9999:
   veri["Yagis"] = 0
yagiss = tk.Label(root, text=veri["Yagis"])
yagiss.grid(row=2, column=1) 

ruzgar_yonu = tk.Label(root, text="Rüzgar yönü").grid(row=3, column=0) 
ruzgar_yonuu = tk.Label(root, text=veri["RuzgarYonu"])
ruzgar_yonuu.grid(row=3, column=1) 

ruzgar = tk.Label(root, text="Rüzgar(km/saat)").grid(row=4, column=0) 
ruzgarr = tk.Label(root, text=veri["Ruzgar_Hizi"])
ruzgarr.grid(row=4, column=1) 

nem = tk.Label(root, text="Nem(%)").grid(row=5, column=0) 
nemm = tk.Label(root, text=veri["Nem"])
nemm.grid(row=5, column=1) 

abasinc = tk.Label(root, text="Aktüel Basınç(hPa)").grid(row=6, column=0)
abasincc = tk.Label(root, text=veri["AktuelBasinc"])
abasincc.grid(row=6, column=1) 

dibasinck = tk.Label(root, text="Denize İndirgenmiş Basınç(hPa)").grid(row=7, column=0)
dibasinckk = tk.Label(root, text=veri["DenizeBasinc"])
dibasinckk.grid(row=7, column=1)
 
durum = tk.Label(root, text="Şu Anki Hava Durumu").grid(row=8, column=0)
durumm = tk.Label(root, text=veri["SuAnkiHavaDurumu"])
durumm.grid(row=8, column=1) 


BosLabel2 = tk.Label(root, text="").grid(row=9, column=0)

tahmin = tk.Label(root, text="Tahmin Edilen Sıcaklık").grid(row=10, column=0)
tahminn = tk.Label(root, text="Henüz Tahmin Edilmedi")
tahminn.grid(row = 10 , column = 1)

BosLabel1 = tk.Label(root, text="").grid(row=11, column=0)

buttonCal = tk.Button(root, text="Tahmin" , command = Tahmin).grid(row=12, column=0)  

OptionMenu(root, clicked, *Sehirler ,command = secim).grid(row=0, column=0)

root.mainloop()  

