import numpy as np


class loss_function:
    def mse(self, act, prediction):
        total = 0
        for i in np.arange(len(act)):
            total += (prediction[i] - act[i]) ** 2
        return total / len(act)
