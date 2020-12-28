#Kütüphanelerin yüklenmesi
import pandas as pd
import numpy as np 

#eksik olan veri dosyasının alınması
eksikVeriler = pd.read_csv("eksikveriler.txt")

from sklearn.impute import SimpleImputer
# eksik verileri tamamlamak için bu şablon kullanılabilir.
#missing_values hangi veriler üzerinde işlem yapılacağını belirliyor
#strategy ise bizim stratejimizi yani seçilen verileri ne ile dolduracağımızı seçiyoruz.
imputer = SimpleImputer(missing_values = np.nan , strategy = 'mean')
Yas = eksikVeriler.iloc[:,1:4].values
print(Yas)

imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)

#-------------------------------------------------------------------

from sklearn import preprocessing
# kategorik verileri sayısal verilere çevirmek için bu şablonlar kullanılabilir.
ulke = eksikVeriler.iloc[:,0:1].values
print(ulke)

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(eksikVeriler.iloc[:,0])
print(ulke)

ohe = preprocessing.OneHotEncoder(categories='auto')
ulke = ohe.fit_transform(ulke).toarray()
print(ulke) 

#------------------------------------------------------------------

#verileri birleştirerek bir veriseti oluşturma.
sonuc = pd.DataFrame(data = ulke , columns=["fr","tr","us"])
print(sonuc)

sonuc2 = pd.DataFrame(data = Yas , columns=["boy","kilo","yas"])
print(sonuc2)

cinsiyet = eksikVeriler.iloc[:,-1].values
print(cinsiyet)

sonuc3 = pd.DataFrame(data = cinsiyet , columns=["cinsiyet"])

s = pd.concat([sonuc , sonuc2 ,sonuc3] , axis = 1)
print(s)
