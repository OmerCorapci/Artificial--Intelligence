import pandas as pd

#bir tane sözlük oluşturuyoruz.
dictionary = {"Name":["omer","hamza","sinan","muhammet","suzan","yuksel"],
              "Yas":[22,20,25,29,40,49],"Maas":[100,150,800,360,1600,2500]}
dataframe = pd.DataFrame(dictionary) #oluşturulan sözlüğü bir pandas dataframe ine çeviriyoruz.
 
print("\nYaş sütunu =\n",dataframe["Yas"])
print("\nFarklı çağırımlı yaş sütunu =\n",dataframe.Yas)
print("\nisim sütunu altında 0-3 arasındaki değerler =\n",dataframe.loc[:3,"Name"])
print("\nİstenilen sütun =\n",dataframe.loc[:3,"Name":"Maas"])


print("----------------------------------------\n\n\n")
print("isim =\n",dataframe.loc[:,"Name"])
print("\n",dataframe.iloc[:,2])  #string olarak belirtmek yerine istenilen stünun kaçıncı stün olduğu sayıyı yazmak yeterli.
dataframe["NewStyle"] = [-1,-2,-5,-10,-16,-100] #dataframe de "NewStyle" diye bir kolon oluşturuluyor ve buna istenilen sayılar ekleniyor.
