import unittest
from fetchPrice import fetchPrice


class MyTestCase(unittest.TestCase):
    '''
    this is the testing file for fetch price and checking that it works as intended.
    author:
     Callan Duffy

    '''

    #
    def type_test(self):
        fetch = fetchPrice()
        self.assertIsInstance(fetch, fetchPrice)

    def test_file_read(self):
        # first test failed content didn't exist
        # second test failed, problem with type
        # third test passed
        fetch = fetchPrice()
        fetch.get_price()
        self.assertTrue(fetch.content['rates'])

    def unpack_test(self):
        # test to check if it does place the dictionary values into the attributes.
        fetch = fetchPrice()
        fetch.get_price()
        fetch.unpack()
        self.assertIsInstance(fetch.euro, float)
        self.assertIsInstance(fetch.usd, float)

    def get_data_test(self):
        # testing to see what we get in return for our dates
        # passed first time
        fetch = fetchPrice()
        result = fetch.get_data("2018-01-01", "2018-01-03")
        self.assertIsInstance(result, dict)


if __name__ == '__main__':
    unittest.main()
