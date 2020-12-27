#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#veriyi yükleme işlemi yapılıyor
veriler = pd.read_csv('maaslar.txt') # veriyi txt dosyasından aldık

#data frame dilimleme(slice)
x = veriler.iloc[:,1:2]
y = veriler.iloc[:,-1:]

#nupmy array uluşturuldu.
X = x.values
Y = y.values

#desicion tree için gerekli kütüphane eklendi.
from sklearn.tree import DecisionTreeRegressor

#decision tree içerisinde de bir kaç farklı algoritma vardır ve bunları sırası ile yaparsak;

r_dt = DecisionTreeRegressor(criterion= 'friedman_mse' ,random_state=  0)
r_dt.fit(X,Y)
plt.scatter(X,Y,color ="red")
plt.plot(x,r_dt.predict(X),color = "black")
plt.show()

r_dt1 = DecisionTreeRegressor(criterion= 'mae' ,random_state=  0)
r_dt1.fit(X,Y)
plt.scatter(X,Y,color ="red")
plt.plot(x,r_dt1.predict(X),color = "black")
plt.show()

r_dt2 = DecisionTreeRegressor(criterion= 'mse' ,random_state=  0)
r_dt2.fit(X,Y)
plt.scatter(X,Y,color ="red")
plt.plot(x,r_dt2.predict(X),color = "black")
plt.show()