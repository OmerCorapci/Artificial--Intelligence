#Gerekli kütüphane eklendi.
import pandas as pd
import numpy as np

#txt doyasındaki bilgiler alındı.
veriler = pd.read_csv("tenis.txt")

#Tahmin edilecek dataframe oluşturuldu.
tahmin = pd.DataFrame(columns =['outlook' , 'temperature' , 'humidity' ,  'windy' , 'play'])
tahmin.loc[0,0:4] = 'rainy' , 'hot', 'high' , 'Truee'

cevapYes = 1
cevapNo = 1

print("\nVerilerimiz\n",veriler)
print("\nCevabını öğrenmek istediğimiz veriler\n",tahmin)

#Kolon başlığının 1 eksiği kadar döngü dönecek.
for i in range(0,(tahmin.shape[1]-1)):
    
    #Bir filtreleme işlemi yapılıyor.
    filtre = veriler.iloc[:,i] == tahmin.iloc[0,i]
    #Verilerde kaç kere oyun oynanmış bulunuyor.
    yes = len(veriler[ veriler['play'] == 'yes'] )
    #Verielrde kaç kere oyun oynanmamış bulunuyor.
    no = len(veriler[ veriler['play'] == 'no'] )
    
    #Filtreli kolonda kaç kere oyun oynanmış ya da oynanmamış bulunuyor.
    cevapYes *= (len (  veriler[filtre][  veriler[filtre]['play'] == 'yes'] ) ) / yes
    cevapNo *= (len (  veriler[filtre][  veriler[filtre]['play'] == 'no'] ) ) / no
    #Ve bütün kolonlar hesaplanarak cevaplar çarpılıyor.
cevapYes *= len(veriler[veriler['play'] == 'yes']) / len(veriler) 
cevapNo *= len(veriler[veriler['play'] == 'no']) / len(veriler)

print("\n---------Tahmin işlemi gerçekleşti ve Sonuç----------")

print("\nCevabın Evet olma ihtimali\n",cevapYes)
print("\nCevabın hayır olma ihtimali\n",cevapNo)

if cevapYes > cevapNo :
    print("\nIşlemler sonucu cevabımız evet'tir ")
    tahmin['play'] = 'yes'
else:
    print("\nIşlemler sonucu cevabımız hayır'dır")
    tahmin['play'] = 'no'
print(tahmin)