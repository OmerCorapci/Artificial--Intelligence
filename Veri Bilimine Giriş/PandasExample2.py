import pandas as pd

dictionary = {"Name":["omer","hamza","sinan","muhammet","suzan","yuksel"],
              "Yas":[22,20,25,29,40,49],"Maas":[100,150,800,360,1600,2500]}
dataframe = pd.DataFrame(dictionary)


filtre = dataframe.Maas < 800
filtre2 = dataframe.Yas < 21

print(dataframe[filtre & filtre2])


a = "omer crp"

print(len(a.split()))