#numpy kütüphanesini ekliyoruz
import numpy as np

array1 = np.array([[1,2,3,],[4,5,6,]]) # array yaratmak için
array2 = np.array([[9,8,7,],[6,5,4,]])

print("1.Array =\n",array1)
print("2.Array =\n",array2)

print("arraylerin toplamı =\n",array1 + array2)
print("arraylerin çarpımı =\n",array1 * array2)

print("arrayın sinüsü alınmış hali =\n",np.sin(array1))

print("array içerisinde 3 den küçük olanlar =\n",array1 < 3)

#5 e 5 boyutunda bir matris oluşturuluyor.
a = np.random.random((5,5)) # 0 ile 1 arasında rastgele sayı üretir

print("Random matris =\n",a)
s
print("Toplamları = \n",a.sum())
print("Aralarındaki en büyük sayı =\n",a.max())
print("Aralarındaki en küçük sayı =\n",a.min())  


print("Satırların toplamı =\n",a.sum(axis = 0))
print("Sütunların toplamı =\n",a.sum(axis = 1)) 