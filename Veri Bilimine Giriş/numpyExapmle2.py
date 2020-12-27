import numpy as np

array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Array = \n",array1)

a = array1.ravel() # arrayi tek boyuta indirger

print("Arrayin tek boyuta indirgenmiş hali =\n",a)

array2 = a.reshape(3,3) #Arrayi istediğimiz matris boyutuna çevirir
print("Arrayin eski hali =\n",array2)

ArrayT = array2.T # Arrayin transpozunu alıyor.
print("Arrayin transpozu\n",ArrayT)

print("arrayin boyutu =\n",array1.shape)