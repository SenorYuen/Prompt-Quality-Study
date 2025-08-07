class StockPortfolioTracker:
    def __init__(self, cash_balance):
        """
        Initialize the StockPortfolioTracker class with a cash balance and an empty portfolio.
        """
        self.cash_balance = cash_balance
        self.portfolio = {}  # Dictionary to store stocks with their quantities

    def add_stock(self, stock):
        """
        Add a stock to the portfolio.
        """
        if stock['name'] not in self.portfolio:
            self.portfolio[stock['name']] = {'quantity': 0, 'price': stock['price']}
        else:
            self.portfolio[stock['name']]['price'] = stock['price']

    def remove_stock(self, stock):
        """
        Remove a stock from the portfolio.
        """
        if stock['name'] in self.portfolio:
            del self.portfolio[stock['name']]

    def buy_stock(self, stock):
        """
        Buy a stock and add it to the portfolio.
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        """
        cost = stock['price'] * stock['quantity']
        if self.cash_balance >= cost:
            if stock['name'] in self.portfolio:
                self.portfolio[stock['name']]['quantity'] += stock['quantity']
            else:
                self.portfolio[stock['name']] = {'quantity': stock['quantity'], 'price': stock['price']}
            self.cash_balance -= cost
            return True
        return False

    def sell_stock(self, stock):
        """
        Sell a stock and remove it from the portfolio and add the cash to the cash balance.
        :return: True if the stock was sold successfully, False if the quantity of the stock is not enough.
        """
        if stock['name'] in self.portfolio and self.portfolio[stock['name']]['quantity'] >= stock['quantity']:
            self.portfolio[stock['name']]['quantity'] -= stock['quantity']
            self.cash_balance += stock['price'] * stock['quantity']
            if self.portfolio[stock['name']]['quantity'] == 0:
                del self.portfolio[stock['name']]
            return True
        return False

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio.
        :return: the total value of the portfolio, float.
        """
        total_value = self.cash_balance
        for stock in self.portfolio.values():
            total_value += stock['quantity'] * stock['price']
        return total_value

    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        """
        summary = []
        for stock_name, stock_data in self.portfolio.items():
            stock_value = stock_data['quantity'] * stock_data['price']
            summary.append({'name': stock_name, 'value': stock_value})
        total_value = self.calculate_portfolio_value()
        return total_value, summary

    def get_stock_value(self, stock):
        """
        Get the value of a stock.
        :return: the value of the stock, float.
        """
        if stock['name'] in self.portfolio:
            return self.portfolio[stock['name']]['quantity'] * self.portfolio[stock['name']]['price']
        return 0.0