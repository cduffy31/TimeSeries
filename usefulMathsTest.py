import unittest
from usefulMaths import usefulMaths

'''
Author:
    Callan Duffy
this is the test class for usefulMaths, it wont be developed in the usual sense, normally tests would be written first
then start writing the code. This will be added to as i go because im not sure what function will be written by me.
'''


class MyTestCase(unittest.TestCase):
    def test_sigmoid(self):
        test = usefulMaths()
        sig = test.sigmoid(1.7)
        self.assertEqual(sig, 0.845534734916)

    def test_relu(self):
        test = usefulMaths()
        relu = test.relu(-1.7)
        self.assertEqual(relu, 0.0)

    def test_tanh(self):
        test = usefulMaths()
        tanh = test.sigmoid(1.7)
        self.assertEqual(tanh, 0.9354090706)

if __name__ == '__main__':
    unittest.main()
