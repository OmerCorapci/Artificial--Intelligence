#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score
#veriyi yükleme işlemi yapılıyor
veriler = pd.read_csv('maaslar.txt') # veriyi txt dosyasından aldık

#data frame dilimleme(slice)
x = veriler.iloc[:,1:2]
y =veriler.iloc[:,-1:]

#nupmy array uluşturuldu.
X = x.values
Y = y.values


#linear regression algoritması uygulanıyor.
#doğrusal model oluşturma
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X,Y)

#polynomial regression
#doğrusal olmayan(nonlinear) model oluşturma.
from sklearn.preprocessing import PolynomialFeatures

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

plt.scatter(X,Y,color = "red")
plt.plot(x,lin_reg.predict(X),color = "blue")
plt.show()


plt.scatter(X,Y,color="red")
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)),color = "blue")
plt.show()


plt.scatter(X,Y,color="red")
plt.plot(X,lin_reg3.predict(poly_reg3.fit_transform(X)),color = "blue")
plt.show()

from sklearn.preprocessing import StandardScaler

sc1 = StandardScaler()
x_olcekli = sc1.fit_transform(X)
sc2 = StandardScaler()
y_olcekli = sc2.fit_transform(Y)

#SVR algoritması ile karar.
from sklearn.svm import SVR

svr_reg = SVR(kernel = 'rbf' )
svr_reg.fit(x_olcekli,y_olcekli)
plt.scatter(x_olcekli,y_olcekli , color = "red")
plt.plot(x_olcekli,svr_reg.predict(x_olcekli), color ="blue")
plt.show()

#desicion tree
from sklearn.tree import DecisionTreeRegressor

r_dt = DecisionTreeRegressor(random_state=  0)
r_dt.fit(X,Y)

plt.scatter(X,Y,color ="red")
plt.plot(x,r_dt.predict(X),color = "black")
plt.show()

#Random Forest
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators=10 , random_state= 0)
rf_reg.fit(X,Y.ravel())

plt.scatter(X,Y,color = "black")
plt.plot(X,rf_reg.predict(X),color ="green")



#ALGORİTMALARIN NASIL ÇALIŞTĞINA DAİR BİLGİLER 'R2'

print("---------------------------------------")

print("Linear R2 değeri")
print(r2_score(Y , lin_reg.predict(X)))

print("Polynomial R2 değeri")
print(r2_score(Y , lin_reg2.predict(poly_reg.fit_transform(X))))

print("SVR R2 değeri")
print(r2_score(y_olcekli ,svr_reg.predict(x_olcekli)))

print("Decision Tree R2 değeri")
print(r2_score(Y ,r_dt.predict(X)))
 
print("Random Forest R2 değeri")
print(r2_score(Y ,rf_reg.predict(X)))