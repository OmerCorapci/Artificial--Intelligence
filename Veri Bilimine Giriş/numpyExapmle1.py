#numpy kütüphanesini ekliyoruz
import numpy as np


array1 = np.array([1,2,3,4,5,6])

print("Array = \n",array1)
print("Arrayın 2. elemanı \n",array1[1])
print("Arrayın ilk 4 elemanı \n",array1[0:4])

print("Arrayın tersi =\n",array1[::-1])

array2 = np.array([[1,2,3,7,8,9],[4,5,6,4,2,1]])

print("2.Array =\n",array2)
print("2.satır 2. sütun =\n",array2[1,1])
print("Bütün satırlar ve 2. sütun \n",array2[:,1])
print("2.satır ve 2-3-4.sütunlar =\n",array2[1,1:4])

print("Arrayın son sütunundaki elemanar =\n",array2[:,-1])
print("Arrayın son satırındaki elemanlar =\n",array2[-1,:])
