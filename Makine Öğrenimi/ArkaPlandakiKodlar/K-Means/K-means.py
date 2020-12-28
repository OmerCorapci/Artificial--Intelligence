#Gerekli kütüphaneler eklendi.
import pandas as pd
import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt
import math

#K yı sabit olarak alıyoruz ama normalde algoritmada kullanıcı giriyor.
# K = 3

#2 nokta arası uzaklığı bulmak için öklit fonksiyonunu yazıyoruz.
def oklit(x1,y1,x2,y2):
    return math.sqrt( (x1-x2)**2 + (y1 - y2)**2 )

#DataFrameini oluşturuyoruz.
#U1 U2 U3 stabil olan 3 adet nokta vardıya o noktalara olan uzaklıkları.U ise en yakın hansinde ise U o oluyor.
df = pd.DataFrame(columns=['X', 'Y','U1','U2','U3','U'])
for i in range(50):#Random 50 adet nokta oluşturuluyor.
    df.loc[i , 0:2] = list(randint(100, size=2)) 

x_veriler = df.iloc[:,0].values
y_veriler = df.iloc[:,1].values

print("X kordinatlar:\n",x_veriler.ravel())
print("Y kordinatlar:\n",y_veriler.ravel())

#aranan adı altında 3 adet x ve y kolonuna sahip dataframe oluşturuyoruz.
aranan = pd.DataFrame(columns=['X','Y'])
#X ve Y kordinatlarını random bir şekilde dolduruyoruz.
for i in range(0,3):
    aranan.loc[i,0:2] = randint(100 , size = 2)

#Verileri görselleştiriyoruz.
plt.scatter(x_veriler,y_veriler,color = 'black')
plt.scatter(aranan.iloc[0,0:1].values , aranan.iloc[0,1:2].values , color = 'red')
plt.scatter(aranan.iloc[1,0:1].values , aranan.iloc[1,1:2].values , color = 'green')
plt.scatter(aranan.iloc[2,0:1].values , aranan.iloc[2,1:2].values , color = 'yellow')
plt.show()

error = 0
#Merkez noktaların eski pozisyonu ile yeni pozisyonu arasında fark var mı diye bir gecici oluşturuyoruz.
gecici = aranan.copy() 

while error != 1 :
    m = 2 
    for i in range (0,3):
        for x in range(0,50):#Bütün noktaların seçili olan 3 noktaya uzaklıkları hesaplanıyor.
            df.loc[x,m:m+1] = oklit(aranan.iloc[i,0:1].values , aranan.iloc[i,1:2].values , df.iloc[x,0:1].values , df.iloc[x,1:2].values)
        m = m + 1
    #Karşılaştırma yaparak en yakın merkez noktasını seçerek U kolon başlığı altına yazılıyor. 
    for i in range(0,50):
        if( df.iloc[i,2:3].values <= df.iloc[i,3:4].values ):
          if( df.iloc[i,2:3].values <= df.iloc[i,4:5].values ):  
              df.loc[i,-1:] = 'U1'
          else:
              df.loc[i,-1:] = 'U3'
        elif( df.iloc[i,3:4].values <= df.iloc[i,4:5].values ):
            df.loc[i,-1:] = 'U2'
        else:
            df.loc[i,-1:] = 'U3'
    
    #Verileri görselleştiriyoruz.
    plt.scatter(df[ df['U'] == 'U1'].iloc[:,0:1].values , df[ df['U'] == 'U1'].iloc[:,1:2].values, color = 'red')
    plt.scatter(df[ df['U'] == 'U2'].iloc[:,0:1].values , df[ df['U'] == 'U2'].iloc[:,1:2].values , color = 'green')
    plt.scatter(df[ df['U'] == 'U3'].iloc[:,0:1].values , df[ df['U'] == 'U3'].iloc[:,1:2].values , color = 'yellow')
    #Merkez noktaları belli olsun diye o renklerin koyu tonlarını seçerek merkezi az çok belli etmeye çalıştım.
    plt.scatter(aranan.iloc[0,0:1].values , aranan.iloc[0,1:2].values , color = 'darkred')
    plt.scatter(aranan.iloc[1,0:1].values , aranan.iloc[1,1:2].values , color = 'darkgreen')
    plt.scatter(aranan.iloc[2,0:1].values , aranan.iloc[2,1:2].values , color = 'brown')
    plt.show()
    
    #Merkez değerleri yeniden hesaplanıyor.
    aranan.loc[0,0:1] = sum(df[ df['U'] == 'U1'].iloc[:,0:1].values) / len( df[ df['U'] == 'U1'] )
    aranan.loc[0,1:2] = sum(df[ df['U'] == 'U1'].iloc[:,1:2].values) / len( df[ df['U'] == 'U1'] )
    
    aranan.loc[1,0:1] = sum(df[ df['U'] == 'U2'].iloc[:,0:1].values) / len( df[ df['U'] == 'U2'] )
    aranan.loc[1,1:2] = sum(df[ df['U'] == 'U2'].iloc[:,1:2].values) / len( df[ df['U'] == 'U2'] )
    
    aranan.loc[2,0:1] = sum(df[ df['U'] == 'U3'].iloc[:,0:1].values) / len( df[ df['U'] == 'U3'] )
    aranan.loc[2,1:2] = sum(df[ df['U'] == 'U3'].iloc[:,1:2].values) / len( df[ df['U'] == 'U3'] )
    #Eski merkez ile yeni merkez arasında fark var mı kontrolü yapılıyor.
    #fark var ise döngü tekrarlanıyor yok ise döngü bitiriliyor.
    if(gecici.iloc[0,0:1].values == aranan.iloc[0,0:1].values and gecici.iloc[0,1:2].values == aranan.iloc[0,1:2].values ):
        if(gecici.iloc[1,0:1].values == aranan.iloc[1,0:1].values and gecici.iloc[1,1:2].values == aranan.iloc[1,1:2].values ):
            if(gecici.iloc[2,0:1].values == aranan.iloc[2,0:1].values and gecici.iloc[2,1:2].values == aranan.iloc[2,1:2].values ):
                error = 1 
                continue
            
    gecici = aranan.copy()