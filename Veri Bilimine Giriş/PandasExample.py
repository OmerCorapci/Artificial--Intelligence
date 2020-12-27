import pandas as pd

dictionary = {"Name":["omer","hamza","sinan","muhammet","suzan","yuksel"],
              "Yas":[22,20,25,29,40,49],"Maas":[100,150,800,360,1600,2500]}

print("Sözlük =\n",dictionary)

dataframe = pd.DataFrame(dictionary) #elimizdeki sözlüğü bir exel verisi gibi veriye dönüştürüyor.
print("dataframe =\n",dataframe)

print("Dataframe deki ilk 5 veriyi gösterir =\n",dataframe.head())

print("Dataframe deki son 5 veriyi gösterir =\n",dataframe.tail())


print("datanın sütun başlıkları =\n",dataframe.columns)

print("istenilen data hakkında ki bilgi =\n",dataframe.info)

print("Veriler ile ilgili ksıa ve öz bilgi veriyor  =\n",dataframe.describe())

print("veri tiplerini ekrana basıyor =\n",dataframe.dtypes)