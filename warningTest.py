import unittest
from warning import warning


"""
for this i can only test that it opens. The rest is just visual inspection.
"""

class MyTestCase(unittest.TestCase):
    def open_test(self):
        warn = warning()
        self.assertIsInstance(warn, warning())


if __name__ == '__main__':
    unittest.main()
