import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from keras.layers import Dense, Dropout
from keras.models import Sequential

df = pd.read_csv("1.csv" , usecols=['OBSERVATORY_NAME',
                                    'DATE_TIME',
                                    'AVERAGE_TEMPERATURE',
                                    'AVERAGE_HUMIDITY', 
                                    'AVERAGE_WIND',
                                    'AVERAGE_DIRECTIONOFWIND',
                                    'AVERAGE_PRECIPITATION'])
df = df[df["OBSERVATORY_NAME"][:] == "UMRANIYE"].sort_values("DATE_TIME")

for i in range (2 , 15):
    
    df1 = pd.read_csv(str(i)+".csv", usecols=['OBSERVATORY_NAME',
                                              'DATE_TIME',
                                              'AVERAGE_TEMPERATURE',
                                              'AVERAGE_HUMIDITY', 
                                              'AVERAGE_WIND',
                                              'AVERAGE_DIRECTIONOFWIND',
                                              'AVERAGE_PRECIPITATION'])
    df1 = df1[df1["OBSERVATORY_NAME"][:] == "UMRANIYE"].sort_values("DATE_TIME")
    df =  pd.concat([df , df1])

df = df.rename(columns = {
    "AVERAGE_TEMPERATURE": " Sıcaklık",
    "AVERAGE_HUMIDITY": "Nem",
    "AVERAGE_WIND": "Rüzgar",
    "AVERAGE_DIRECTIONOFWIND": "Rüzgar Yönü",
    "AVERAGE_PRECIPITATION": "Yağış",
})

df = df.drop(["OBSERVATORY_NAME" , "DATE_TIME"] , axis = 1)

y = df.iloc[1:7077,0].values.reshape((7076,1))
df = df.iloc[0:7076,:]

X_train, X_test, y_train, y_test = train_test_split(df, y, test_size =0.0001, random_state = 42)

model = Sequential()

model.add(Dense(units = 32, kernel_initializer = 'uniform', activation = 'relu', input_dim = 5))
model.add(Dense(units = 32, kernel_initializer = 'uniform', activation = 'relu'))
model.add(Dropout(0.25))
model.add(Dense(units = 16, kernel_initializer = 'uniform', activation = 'relu'))
model.add(Dropout(0.25))
model.add(Dense(units = 16, kernel_initializer = 'uniform', activation = 'relu'))
model.add(Dense(units = 16, kernel_initializer = 'uniform', activation = 'relu'))
model.add(Dropout(0.3))
model.add(Dense(units = 8, kernel_initializer = 'uniform', activation = 'relu'))
model.add(Dense(units = 1))

model.compile(optimizer = 'rmsprop', loss = 'mse', metrics = ['mae'])

model.fit(X_train, y_train, batch_size = 10, epochs = 35, validation_split=0.3)

model.save("model")
