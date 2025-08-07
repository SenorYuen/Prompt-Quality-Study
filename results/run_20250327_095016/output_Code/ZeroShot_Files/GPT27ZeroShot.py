class CurrencyConverter:
    def __init__(self):
        """
        Initialize the exchange rate of the US dollar against various currencies
        """
        # Dictionary to store currency rates where key is currency code and value is the exchange rate
        self.exchange_rates = {
            'USD': 1.0,  # Base currency
            'EUR': 0.85,
            'JPY': 110.0,
            'GBP': 0.75,
            'AUD': 1.35
        }

    def convert(self, amount, from_currency, to_currency):
        """
        Convert the value of a given currency to another currency type
        :return: float, value converted to another currency type
        """
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("Currency not supported")
        
        # Convert amount to USD first
        amount_in_usd = amount / self.exchange_rates[from_currency]
        # Convert USD to target currency
        converted_amount = amount_in_usd * self.exchange_rates[to_currency]
        return converted_amount

    def get_supported_currencies(self):
        """
        Returns a list of supported currency types
        :return: list, All supported currency types
        """
        return list(self.exchange_rates.keys())

    def add_currency_rate(self, currency, rate):
        """
        Add a new supported currency type, return False if the currency type is already in the support list
        :return: If successful, returns None; if unsuccessful, returns False
        """
        if currency in self.exchange_rates:
            return False
        self.exchange_rates[currency] = rate

    def update_currency_rate(self, currency, new_rate):
        """
        Update the exchange rate for a certain currency
        :return: If successful, returns None; if unsuccessful, returns False
        """
        if currency not in self.exchange_rates:
            return False
        self.exchange_rates[currency] = new_rate