import pandas as pd
import numpy as np 

veriler = pd.read_csv("veriler.txt")

x = veriler.iloc[:,1:4].values
y = veriler.iloc[:,-1:].values

from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)


from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
gnb.fit(x_train , y_train)

y_pred = gnb.predict(x_test)

print("Gerçek veri\n",y_test.ravel())
print("Tahmin edilen veri\n",y_pred)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test,y_pred)
print('GNB')
print(cm)