#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#veriyi yükleme işlemi yapılıyor
veriler = pd.read_csv('maaslar.txt') # veriyi txt dosyasından aldık

#nupmy array uluşturuldu.
X = veriler.iloc[:,1:2].values
Y = veriler.iloc[:,-1:].values

#Random Forest
from sklearn.ensemble import RandomForestRegressor

rf_reg = RandomForestRegressor(n_estimators=10 , random_state= 0)
rf_reg.fit(X,Y.ravel())
plt.scatter(X,Y,color = "black")
plt.plot(X,rf_reg.predict(X),color ="green")