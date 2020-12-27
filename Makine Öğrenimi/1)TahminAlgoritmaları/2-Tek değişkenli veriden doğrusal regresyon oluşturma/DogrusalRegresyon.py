#kütüphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#veri yükleme
veriler = pd.read_csv('satislar.txt')

#veri ön isleme
aylar = veriler[['Aylar']]
print(aylar)

satislar = veriler[['Satislar']]
print(satislar)

satislar2 = veriler.iloc[:,:1].values
print(satislar2)

#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split
#test_size test için ayrılacak olan verinin % kaç olacağıdır.
#random_state belirlersek test verimiz her zaman aynı şekilde belirlenir 
#eğer belirlemezsek test verisi her zaman değişir .Bu herhangi bir sayı olabilir.
x_train, x_test,y_train,y_test = train_test_split(aylar,satislar,test_size=0.33, random_state=0)

#model inşası
#Doğrusal regresyon için gerekli kütüphane ekleniyor
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x_train,y_train) #model oluşturulmaya çalışılıyor

tahmin = lr.predict(x_test)


#verileri soralıyoruz.
#çünkü grafik üzerinde güzel bir şekilde gözüksün diyedir.
x_train = x_train.sort_index()
y_train = y_train.sort_index()

plt.plot(x_train,y_train)
plt.plot(x_test , lr.predict(x_test)) #tahmin zaten linner bir doğru olacağı için sıralamaya gerek duyulmuyor.