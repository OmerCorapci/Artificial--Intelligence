import pandas as pd
import numpy as np 

veriler = pd.read_csv("veriler.txt")

x = veriler.iloc[:,1:4].values
y = veriler.iloc[:,-1:].values

#eğitmek ve test etmek için gerekli kütüphane ekleniyor.
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=10)

#KNN algoritması.
from sklearn.neighbors import KNeighborsClassifier

#n_neighbors : bakılacak olan komşuları belirler.
knn = KNeighborsClassifier(n_neighbors= 7 , metric = 'minkowski')
knn.fit(x_train , y_train)

from sklearn.metrics import confusion_matrix

y_pred = knn.predict(x_test)

cm = confusion_matrix(y_test, y_pred)
print("Confusion matrix :\n",cm)

print("Tahmin edilecek gerçek verimiz :\n",y_test.ravel())
print("Tahmin edilen :\n",y_pred)