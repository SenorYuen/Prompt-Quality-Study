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
        if from_currency in self.rates and to_currency in self.rates:
            return amount / self.rates[from_currency] * self.rates[to_currency]
        else:
            return None

    def get_supported_currencies(self):
        return list(self.rates.keys())

    def add_currency_rate(self, currency, rate):
        if currency not in self.rates:
            self.rates[currency] = rate
            return None
        else:
            return False

    def update_currency_rate(self, currency, new_rate):
        if currency in self.rates:
            self.rates[currency] = new_rate
            return None
        else:
            return False