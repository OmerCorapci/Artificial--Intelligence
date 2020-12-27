#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#veriyi yükleme işlemi yapılıyor
veriler = pd.read_csv('maaslar.txt') # veriyi txt dosyasından aldık

#data frame imizi dilimledik(slice).
x = veriler.iloc[:,1:2]
y = veriler.iloc[:,-1:]

#nupmy array uluşturuldu.
X = x.values
Y = y.values


#doğrusal regresyon kütüphanesini ekliyoruz.
from sklearn.linear_model import LinearRegression
#model oluşturuluyor.
lin_reg = LinearRegression()
lin_reg.fit(X,Y)#modeli eğitiyoruz.

#polinomal regresyon
#doğrusal olmayan(nonlinear) model oluşturma.
from sklearn.preprocessing import PolynomialFeatures

#degree = polinomun kaç dereceden oluşturulacağı belirleniyor.
poly_reg = PolynomialFeatures(degree = 2)#2.dereceden bir polinomal obje oluşturuldu.
x_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)

#4.dereceden bir polinomal obje oluşturuldu.
poly_reg3 = PolynomialFeatures(degree = 4)
x_poly3 = poly_reg3.fit_transform(X)
lin_reg3 = LinearRegression()
lin_reg3.fit(x_poly3,y)

#Görselleştirme

#doğrusal regresyon modeli.
plt.scatter(X,Y,color = "red")
plt.plot(x,lin_reg.predict(X),color = "blue")
plt.show()

#2.dereceden polinom modeli
plt.scatter(X,Y,color="red")
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)),color = "blue")
plt.show()

#4.dereceden polinom modeli
plt.scatter(X,Y,color="red")
plt.plot(X,lin_reg3.predict(poly_reg3.fit_transform(X)),color = "blue")
plt.show()