from usefulMaths import usefulMaths
import numpy as np


class lstm:
    def __init__(self):
        # weights for computation
        self.wf = np.random.rand(1, 2)
        self.bf = np.random.rand()
        self.wi = np.random.rand(1, 2)
        self.ui = np.random.rand(1, 2)
        self.bi = np.random.rand()
        self.ci = np.random.rand()
        self.wo = np.random.rand(1, 2)
        self.bo = np.random.rand()
        self.maths = usefulMaths()

    def lstm_cell(self, carry, prev_ht, inputs):
        f = self.forget_layer(inputs, prev_ht)
        i, c = self.input_layer(inputs, prev_ht)
        carry = self.cell_state(carry, i, f, c)
        output = self.output_layer(inputs, prev_ht)
        output = output * self.maths.relu(carry)
        return carry, output

    def forget_layer(self, inputs, prev):
        return self.maths.sigmoid(np.dot([inputs, prev], self.wf) + self.bf)

    def input_layer(self, inputs, prev):
        return self.maths.sigmoid(np.dot([inputs, prev], self.wi) + self.bi), self.maths.relu(np.dot([input, prev],
                                                                                                     self.ui) + self.ci)

    def cell_state(self, carry, inputs, forget, c):
        return (forget * carry) + (inputs * c)

    def output_layer(self, inputs, prev):
        return self.maths.sigmoid(np.dot([inputs, prev], self.wo) + self.bo)
