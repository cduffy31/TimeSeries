'''
this file is to check whether the concept of a long short term algorithm will work on our data set

author:
    Callan Duffy
param:
    csv data set
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.preprocessing.sequence import TimeseriesGenerator
# importing the test data from the folder
df = pd.read_csv('TestData.csv')

# creating a new dataframe that only has type date and the closing price.
# this is because they're the only values we care about.
df['Date'] = pd.to_datetime(df['Date'])
df.set_axis(df['Date'], inplace=True)
# deletes anything not related to the closing price
df.drop(columns=['Open', 'High', 'Low', 'Last', 'Total Trade Quantity', 'Turnover (Lacs)'], inplace=True)

# converting dataset into x_train and y_train


close_data = df['Close'].values
close_data = close_data.reshape((-1, 1))

split_percent = 0.80
split = int(split_percent * len(close_data))

close_train = close_data[:split]
close_test = close_data[split:]

date_train = df['Date'][:split]
date_test = df['Date'][split:]

look_back = 15
# the lstm will look back at the previous 15
train_generator = TimeseriesGenerator(close_train, close_train, length=look_back, batch_size=20)
test_generator = TimeseriesGenerator(close_test, close_test, length=look_back, batch_size=1)

test_model = Sequential()
test_model.add(LSTM(10, activation='relu', input_shape=(look_back, 1)))
test_model.add(Dense(1))
test_model.compile(optimizer='adam', loss='mse')

num_epochs = 25
test_model.fit_generator(train_generator, epochs=num_epochs, verbose=1)
test_model.summary()

prediction = test_model.predict_generator(test_generator)

plt.plot(np.arange(prediction.shape[0]), prediction[:, 0], label='prediction')
plt.plot(np.arange(close_test.size), close_test, label='actual')
plt.xlabel('day')
plt.ylabel('price')
plt.legend()
plt.savefig('lstmTestResults.png')
