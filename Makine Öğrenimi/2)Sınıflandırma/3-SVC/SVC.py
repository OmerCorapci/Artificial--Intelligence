import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

veriler = pd.read_csv("veriler.txt")

x = veriler.iloc[:,1:4].values
y = veriler.iloc[:,-1:].values

from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=5)

from sklearn.svm import SVC

svc = SVC(kernel= 'poly')
svc.fit(x_train , y_train)

y_pred = svc.predict(x_test)

print("Gerçek veri\n",y_test.ravel())
print("Tahmin edilen veri\n",y_pred)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test,y_pred)
print('SVC')
print(cm) 