#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#veriyi yükleme işlemi yapılıyor
veriler = pd.read_csv('maaslar.txt') # veriyi txt dosyasından aldık

#nupmy array uluşturuldu.
X = veriler.iloc[:,1:2].values
Y = veriler.iloc[:,-1:].values

#NOT : SVR da verimizi ölçeklendirmemiz gerekiyor.

#ölçeklemek için gerekli kütüphane ekleniyor.
from sklearn.preprocessing import StandardScaler

sc1 = StandardScaler()

x_olcekli = sc1.fit_transform(X)
print("x ölçekli\n",x_olcekli)
sc2 = StandardScaler()
y_olcekli = sc2.fit_transform(Y)
print("y ölçekli\n",y_olcekli)

#SVR algoritması ile karar.
from sklearn.svm import SVR

#SVR ın içerisinde bir kaç algoritma vardır bunlar "rbf , poly sigmoid"
#hepsini denerisek;

svr_reg = SVR(kernel = 'rbf' )
svr_reg.fit(x_olcekli,y_olcekli)
plt.scatter(x_olcekli,y_olcekli , color = "red")
plt.plot(x_olcekli,svr_reg.predict(x_olcekli), color ="blue")
plt.show()

svr_reg = SVR(kernel = 'poly' )
svr_reg.fit(x_olcekli,y_olcekli)
plt.scatter(x_olcekli,y_olcekli , color = "red")
plt.plot(x_olcekli,svr_reg.predict(x_olcekli), color ="blue")
plt.show()

svr_reg = SVR(kernel = 'sigmoid' )
svr_reg.fit(x_olcekli,y_olcekli)
plt.scatter(x_olcekli,y_olcekli , color = "red")
plt.plot(x_olcekli,svr_reg.predict(x_olcekli), color ="blue")
plt.show()