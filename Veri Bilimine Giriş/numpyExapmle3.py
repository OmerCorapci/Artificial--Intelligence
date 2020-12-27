#numpy kütüphanesini ekliyoruz
import numpy as np

array1 = np.array([[1,2],[4,5]])
array2 = np.array([[-9,7],[5,-2]])

print("1.array =\n",array1)
print("2.array =\n",array2)


#veritical yani dikey birleştirme
array3 = np.vstack((array1,array2))
print("Arraylerin dikey birleştirilmiş hali =\n",array3)

#horizontal yani yatay birleştirme

array4 = np.hstack((array1,array2))
print("Arraylerin yatay birleştirilmiş hali =\n",array4)

print("-------------------------------------------------")

liste = [1,5,3,9]

array = np.array(liste)
print("liste = ",liste)
print("Array =\n",array)

liste2 = list(array)

#eğer direkt a = array deseydik arrayde olan değişiklik a yı da etkileyecekti.
#a aslında bir kısayol görevi görecekti.
#Ama .copy fonksiyonunu kullandığımızda onun kopyasını çıkarıyor.
a = array.copy()
print("Arrayin kopyası =\n",a)