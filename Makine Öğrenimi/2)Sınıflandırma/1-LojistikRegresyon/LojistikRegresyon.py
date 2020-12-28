import pandas as pd
import numpy as np 

veriler = pd.read_csv("veriler.txt")

x = veriler.iloc[:,1:4].values
y = veriler.iloc[:,-1:].values

#eğitmek ve test etmek için gerekli kütüphane ekleniyor.
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=10)

#gerekli olan kütüphaneyi ekliyoruz.
from sklearn.linear_model import LogisticRegression

#modelimizi inşa ediyoruz.
logr = LogisticRegression(random_state= 0)
logr.fit(x_train,y_train)#modeli eğitiyoruz.

y_pred = logr.predict(x_test)

print("Gerçek veri\n",y_test.ravel())
print("Tahmin edilen veri\n",y_pred)

#Verileri ne kadar doğru ne kadar yanlış tahmin etmişiz onu bilmek için
#bu kütüphaneyi ekliyoruz.
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test ,y_pred)
print(cm)