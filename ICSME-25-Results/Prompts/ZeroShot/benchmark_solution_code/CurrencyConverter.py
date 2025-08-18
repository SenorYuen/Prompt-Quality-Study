'''
# This is a class for currency conversion, which supports to convert amounts between different currencies, retrieve supported currencies, add new currency rates, and update existing currency rates.

class CurrencyConverter:
    def __init__(self):
        """
        Initialize the exchange rate of the US dollar against various currencies
        """
        }

    def convert(self, amount, from_currency, to_currency):
        """
        Convert the value of a given currency to another currency type
        :return: float, value converted to another currency type
        """


    def get_supported_currencies(self):
        """
        Returns a list of supported currency types
        :return:list, All supported currency types
        """


    def add_currency_rate(self, currency, rate):
        """
        Add a new supported currency type, return False if the currency type is already in the support list
        :return:If successful, returns None; if unsuccessful, returns False
        """


    def update_currency_rate(self, currency, new_rate):
        """
        Update the exchange rate for a certain currency
        :return:If successful, returns None; if unsuccessful, returns False
        """
'''


class CurrencyConverter:
    def __init__(self):
        self.rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.72,
            'JPY': 110.15,
            'CAD': 1.23,
            'AUD': 1.34,
            'CNY': 6.40,
        }

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount

        if from_currency not in self.rates or to_currency not in self.rates:
            return False

        from_rate = self.rates[from_currency]
        to_rate = self.rates[to_currency]

        converted_amount = (amount / from_rate) * to_rate
        return converted_amount

    def get_supported_currencies(self):
        return list(self.rates.keys())

    def add_currency_rate(self, currency, rate):
        if currency in self.rates:
            return False
        self.rates[currency] = rate

    def update_currency_rate(self, currency, new_rate):
        if currency not in self.rates:
            return False
        self.rates[currency] = new_rate
