class CurrencyConverter:
    def __init__(self):
        # Initialize the exchange rate of the US dollar against various currencies
        self.exchange_rates = {
            'USD': 1.0,  # Base currency
            'EUR': 0.88,  # 1 USD = 0.88 EUR
            'GBP': 0.76,  # 1 USD = 0.76 GBP
            'JPY': 114.74,  # 1 USD = 114.74 JPY
            'CNY': 6.47,  # 1 USD = 6.47 CNY
        }

    def convert(self, amount, from_currency, to_currency):
        # Check if both currencies are supported
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("One or both currencies are not supported")
        
        # Convert the amount to USD first
        usd_amount = amount / self.exchange_rates[from_currency]
        
        # Then convert the USD amount to the target currency
        converted_amount = usd_amount * self.exchange_rates[to_currency]
        
        return converted_amount

    def get_supported_currencies(self):
        # Returns a list of supported currency types
        return list(self.exchange_rates.keys())

    def add_currency_rate(self, currency, rate):
        # Check if the currency is already supported
        if currency in self.exchange_rates:
            return False  # Return False if the currency is already supported
        
        # Add the new currency rate
        self.exchange_rates[currency] = rate
        return None

    def update_currency_rate(self, currency, new_rate):
        # Check if the currency is supported
        if currency not in self.exchange_rates:
            return False  # Return False if the currency is not supported
        
        # Update the exchange rate for the currency
        self.exchange_rates[currency] = new_rate
        return None