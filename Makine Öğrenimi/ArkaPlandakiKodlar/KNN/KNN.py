#Gerekli kütüphaneler ekleniyor.
import pandas as pd
import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt
import math

#Noktalar arası uzaklığı ölçmek için gerekli olan öklit fonksiyonu yazılıyor.
def oklit(x1,y1,x2,y2):
    return math.sqrt( (x1-x2)**2 + (y1 - y2)**2 )
    
#Gerekli olan dataframe oluşturuluyor.
df = pd.DataFrame(columns=['X', 'Y', 'Derece' , 'Oklid'])
for i in range(30):
    df.loc[i , 0:3] = list(randint(100, size=2)) + list(randint(30 , size=1)) 

x_veriler = df.iloc[:,0].values
y_veriler = df.iloc[:,1].values
dereceler = df.iloc[:,2].values
print("\nX kordinatları\n",x_veriler.ravel())
print("\nY kordinatları\n",y_veriler.ravel())
print("\nNoktaların sahip olduğu dereceler(Puanda diyebiliriz)\n",dereceler.ravel())

#Rastgele bir nokta datafremi i oluşturuyoruz .
#Gördüğnüüz gibi içerisinde 1 adet veri var biz bunun derecesini(Puanını)bulmaya çalışacağız.
df1 = pd.DataFrame(columns=['X', 'Y', 'Derece'])
df1.loc[0,0:2] = randint(100, size=2)


X = df1.iloc[0,0:1].values
Y = df1.iloc[0,1:2].values
print("\nPuanını bulmak istediğimiz noktanın X kordinatı \n",X)
print("\nPuanını bulmak istediğimiz noktanın Y kordinatı \n",Y)

plt.scatter(x_veriler,y_veriler,color = "black")
plt.scatter(X,Y, color = 'red')

#bütün verilerin noktaya uzaklığı hesaplanıyor.
for i in range(0,30):
    df.iloc[i ,-1:] = oklit(X , Y , x_veriler[i] , y_veriler[i])
    
df = df.sort_values(['Oklid'])
print("\nSeçilen noktaya en yakın 3 nokta \n",df.iloc[0:3,:])
df1.iloc[0,-1:] = (( df.iloc[0, 2:3].values +df.iloc[1, 2:3].values + df.iloc[2, 2:3].values ) /3 )
print("\nSeçilen nokta \n",df1)