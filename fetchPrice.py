from exchangeratesapi import Api
from datetime import datetime


class fetchPrice:
    """
    This class is using the central european banks API to get up to date prices of foreign exchange
    Author:
        Callan Duffy
    param:
        doesnt require anything but can use dates if required.
        dates must be added as "yyyy-mm-dd", this is to keep the format friendly for python dictionary
    return:
        can either return a couple or a numpy array depending on what is asked.
    """

    def __init__(self):
        # content becomes a dictionary
        self.content = None
        self.euro = 0
        self.usd = 0
        self.api = Api()

    def get_price(self):
        # opening the url and receiving the JSON object to the allow the class its self to use it
        self.content = self.api.get_rates('GBP', ['USD', 'EUR'])
        self.unpack()

    def unpack(self):
        self.euro = self.content['rates']['EUR']
        self.usd = self.content['rates']['USD']

    def get_data(self, start, end):
        # returns a dictionary so wont be on a sorted order
        return self.api.get_rates('GBP', ['USD', 'EUR'], start, end)

    def get_more(self, currencies, start, end):
        # currencies is a list of currencies that the user wants the data for.
        return self.api.get_rates('GBP', currencies, start, end)
