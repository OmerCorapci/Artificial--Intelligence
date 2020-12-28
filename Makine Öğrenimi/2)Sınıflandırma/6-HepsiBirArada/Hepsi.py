import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#veriler = pd.read_csv("C:\\Users\\Omer\\Desktop\\makineOgrenmesi\\veriler")
veriler = pd.read_csv("veriler.txt")

x = veriler.iloc[:,1:4].values
y = veriler.iloc[:,-1:].values

from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)

#gerekli olan kütüphaneyi ekliyoruz.
from sklearn.linear_model import LogisticRegression

#modelimizi inşa ediyoruz.
logr = LogisticRegression(random_state= 0)
logr.fit(x_train,y_train)#modeli eğitiyoruz.

y_pred = logr.predict(x_test)

print("\nLojistik Regresyon")
print("Gerçek veri\n",y_test.ravel())
print("Tahmin edilen veri\n",y_pred)

#Verileri ne kadar doğru ne kadar yanlış tahmin etmişiz onu bilmek için
#bu kütüphaneyi ekliyoruz.
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test ,y_pred)
print(cm,"\n")


#KNN algoritması.
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors= 1 , metric = 'minkowski')
knn.fit(x_train , y_train)

y_pred = knn.predict(x_test)

print("KNN")
print("Gerçek veri\n",y_test.ravel())
print("Tahmin edilen veri\n",y_pred)


cm = confusion_matrix(y_test , y_pred)
print(cm,"\n")

from sklearn.svm import SVC

svc = SVC(kernel= 'poly')
svc.fit(x_train , y_train)

y_pred = svc.predict(x_test)

print("SVC")
print("Gerçek veri\n",y_test.ravel())
print("Tahmin edilen veri\n",y_pred)

cm = confusion_matrix(y_test,y_pred)
print(cm,"\n")

from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
gnb.fit(x_train , y_train)

y_pred = gnb.predict(x_test)

print("Naive Bayes")
print("Gerçek veri\n",y_test.ravel())
print("Tahmin edilen veri\n",y_pred)

cm = confusion_matrix(y_test,y_pred)
print(cm,"\n")

from sklearn.tree import DecisionTreeClassifier

dct = DecisionTreeClassifier(criterion ='entropy')

dct.fit(x_train , y_train)
y_pred = dct.predict(x_test)

print("Decision Tree")
print("Gerçek veri\n",y_test.ravel())
print("Tahmin edilen veri\n",y_pred)

cm = confusion_matrix(y_test , y_pred)
print(cm,"\n")