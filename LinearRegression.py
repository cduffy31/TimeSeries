import numpy as np
import pandas as pd
import math as math
import matplotlib
import matplotlib.pyplot as plt
from GetData import get_daily_data


def get_data():
    data = np.array(get_daily_data())
    data_len = len(data)
    training_data = data[:math.floor(data_len * 0.75)]
    test_data = data[math.ceil(data_len * 0.75):]
    return [training_data, test_data]


# print(data)

def weekly_array(x):
    for i in range(len(x)):
        x[i] = 7 * i
    return x


def mean(array):
    s = y_sum(array)
    float(s)
    length = len(array)
    float(length)
    return s / length


def variance(array):
    m = mean(array)
    return sum([(x - m) ** 2 for x in array])


def covariance(x, x_mean, y, y_mean):
    cvar = 0.0
    for i in range(len(x)):
        cvar += (x[i] - x_mean) * (y[i] - y_mean)
    return cvar


def y_sum(array):
    total = 0
    for i in range(len(array)):
        total = total + int(array[i])
    return total


def coef(dat):
    X = weekly_array(dat[:, 0]).astype(np.float)
    Y = dat[:, 1].astype(np.float)
    # print(X)
    # print(Y) placed for testing only
    y_mean = mean(Y)
    x_mean = X / len(X)  # weekly data
    x_variance = variance(X)
    covar = covariance(X, x_mean, Y, y_mean)
    coef1 = covar / x_variance
    coef2 = y_mean - coef1 * x_mean
    date = X[-1]
    return [coef1, coef2, date]


def linear_regression(training_set, test_set):
    predictions = list()
    coef1, coef2, date = coef(training_set)
    for row in test_set:
        y = coef1 + coef2 * (date+7)
        y = y/100
        predictions.append(y)
    return predictions


def run():
    training_data, test_data = get_data()
    predictions = linear_regression(training_data, test_data)
    print(test_data)
    print(predictions)


run()
