#kutuphaneler
import numpy as np
import pandas as pd

veriler = pd.read_csv('veriler.txt') # veriyi txt dosyasından aldık

print(veriler)
boyKiloYas = veriler.iloc[:,1:4].values 

print("Boy Kilo ve Yaş verisi \n",boyKiloYas)

ulke = veriler.iloc[:,0:1].values
print("Ülke verisinin kategorik hali \n",ulke)

#kategorik veriyi sayısal veriye dönüştürüyoruz.
from sklearn import preprocessing

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])

print("Ülke verisinin sayısal hali\n",ulke)

ohe = preprocessing.OneHotEncoder(categories='auto')
ulke = ohe.fit_transform(ulke).toarray()
print("Ülke verisinin hem sayısal hemde düzenlenmiş hali\n",ulke)

c = veriler.iloc[:,-1:].values
print("Cinsiyet verisinin kategorik hali\n",c)


c[:,-1] = le.fit_transform(veriler.iloc[:,-1])

#NOT burada gördüğünüz gibi cinsiyeti 2 kolona ayırmıyoruz bunun sebebi ise;
#cinsiyet bildiğiniz gibi ya erkek dir ya da kadın . Bizim verimize göre tabiki.
#Yani ya 0 ya da 1 olarak verebiliriz . Ayrı ayrı kolonlara ayırmamıza gerekyoktur.
print("Cinsiyet verisinin sayısal hali\n",c)


#numpy dizileri dataframe donusumu
sonuc = pd.DataFrame(data=ulke, index = range(22), columns = ['fr','tr','us'])
print("Ülke verisini dataFrame e dönüştürüyoruz\n",sonuc)

sonuc2 = pd.DataFrame(data=boyKiloYas, index = range(22), columns = ['boy','kilo','yas'])
print("boyKiloYas verisini dataFrame e dönüştürüyoruz\n",sonuc2)

cinsiyet = veriler.iloc[:,-1].values
print("Cinsiyet kolonunu ekrana basıyoruz\n",cinsiyet)

sonuc3 = pd.DataFrame(data = c[:,:1], index = range(22), columns = ['cinsiyet'])
print("Cinsiyet verisini dataFrame e dönüştürüyoruz\n",sonuc3)


#dataframe birlestirme islemi
s=pd.concat([sonuc,sonuc2], axis=1)
print("Ülke dataframe i ile boyKiloYas dataframe i birleştiriyoruz\n",s)

s2=pd.concat([s,sonuc3], axis=1)
print("İlk birleştirdiğimiz dataframe e cinsiyet dataframe ini de ekliyoruz\n",s2)


#Bütün verilerden boy verisini öğrenmek istiyoruz bunun için önce boy verisini çekiyoruz.
boy = s2.iloc[:,3:4].values
print("Boy verisi\n",boy)

#boy verisi harici diğer verileri alıyoruz
sol = s2.iloc[:,:3]
sag = s2.iloc[:,4:]

#Ve bunları birleştiriyoruz.
veri = pd.concat([sol,sag],axis=1)

#eğitmek için gerekli kütüphaneyi ekliyoruz.
from sklearn.model_selection import train_test_split
#verilerin egitim ve test icin bolunmesi
#test_size test için ayrılacak olan verinin % kaç olacağıdır.
#random_state belirlersek test verimiz her zaman aynı şekilde belirlenir 
#eğer belirlemezsek test verisi her zaman değişir .Bu herhangi bir sayı olabilir.
x_train, x_test,y_train,y_test = train_test_split(veri,boy,test_size=0.33, random_state=0)

#Doğrusal regresyon kütüphanesini ekliyoruz
from sklearn.linear_model import LinearRegression

#modeli oluşturuyoruz.
r2 = LinearRegression()
r2.fit(x_train,y_train)#trainlerle modelimizi eğitiyoruz.

y_pred = r2.predict(x_test)#x_test i vererek y nin ne olabileceğini tahmin ediyor.

#Model hakkında bilgi almak için gerekli kütüphaneyi ekliyoruz.
import statsmodels.api as sm

#Buradaki amacımız verilerin " p>|t| " değerlerine bakarak hangileri bizim için uygundur onu öğrenmektir.
#0 dan uzaklaşıyor ise bu veri bizim için kötüleşiyor ve çıkartmamız gerektiğini öğreniyoruz. 

#Burada gördük ki x5 verisi yani 4. veri bizim için problemli ve bunu modelimizden çıkardık ve devam ettik.

X_l = veri.iloc[:,[0,1,2,3,4,5]].values
X_l = np.array(X_l,dtype = float)
model = sm.OLS(boy,X_l).fit()
print(model.summary())

#Burada gördük ki yeni x5 değeri yani ona karşılık 5. verimiz de 0 dan uzaklaşıyor aslında çok küçük bir sayı
#çıkarmazsak da olur . İsteğimize bağlır bir durumdur.

X_l = veri.iloc[:,[0,1,2,3,5]].values
X_l = np.array(X_l,dtype = float)
model = sm.OLS(boy,X_l).fit()
print(model.summary())

#En uygun modelimizi bulmuş olduk.

X_l = veri.iloc[:,[0,1,2,3]].values
X_l = np.array(X_l,dtype = float)
model = sm.OLS(boy,X_l).fit()
print(model.summary())