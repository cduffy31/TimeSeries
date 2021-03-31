import math

'''
Author:
    Callan Duffy
this is a class to hold useful mathematical functions. it will be added to as necessary
sigmoid: f(x) = 1/(1+e^-x)
relu: f(x) = max(0, x)
tanh: f(x) = 2/(1+e^-2x) - 1 
'''


class usefulMaths:

    def __init__(self, *args, **kwargs):
        self

    def sigmoid(self, x):
        return round((1 / (1 + math.exp(-x))), 12)

    def relu(self, x):
        return max(0.0, x)

    def tanh(self, x):
        return math.tanh(x)
