import numpy as np
import math as m

'''
this is the adam optimizer taken from "Adam: A Method for Stochastic Optimization" written by Diederik P. Kingma and 
Jimmy Ba. ive implemented from scratch using their suggested parameters
this when implemented will update the weights. i chose to implement as a class so when the training is over the values 
are saved. 

'''


class optimizer:
    def __init__(self):
        self.alpha = 0.01  # learning rate
        self.beta_a = 0.9
        self.beta_b = 0.999
        self.e = 1e-8  # 0.00000001
        self.theta = 0
        self.mt = 0
        self.vt = 0
        self.t = 0
        self.last_theta = 0
        while self.last_theta != self.theta:
            self.t += 1
            gt = self.grad_func(self.theta)
            self.mt = self.beta_a * self.mt + (1 - self.beta_a) * gt
            self.vt = self.beta_b * self.vt + (1 - self.beta_b) * (gt ** 2)
            m = self.mt / (1 - (self.beta_a ** self.t))
            v = self.vt / (1 - (self.beta_b ** self.t))
            self.last_theta = self.theta
            self.theta = self.theta - (self.alpha * m) / (m.sqrt(v) + self.e)

    def grad(self, x):
        return x * x - 4 * x + 4

    def grad_func(self, x):
        return 2 * x - 4
