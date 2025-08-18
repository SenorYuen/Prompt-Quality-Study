'''
# This is a class as StockPortfolioTracker that allows to add stocks, remove stocks, buy stocks, sell stocks, calculate the total value of the portfolio, and obtain a summary of the portfolio.

class StockPortfolioTracker:
    def __init__(self, cash_balance):
        """
        Initialize the StockPortfolioTracker class with a cash balance and an empty portfolio.
        """

    def add_stock(self, stock):
        """
        Add a stock to the portfolio.

        """

    def remove_stock(self, stock):
        """
        Remove a stock from the portfolio.
       

        """

    def buy_stock(self, stock):
        """
        Buy a stock and add it to the portfolio.
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        """

    def sell_stock(self, stock):
        """
        Sell a stock and remove it from the portfolio and add the cash to the cash balance.
        :return: True if the stock was sold successfully, False if the quantity of the stock is not enough.
        """

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio.
        :return: the total value of the portfolio, float.
        """

    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        """

    def get_stock_value(self, stock):
        """
        Get the value of a stock.
        :return: the value of the stock, float.

        """
'''


class StockPortfolioTracker:
    def __init__(self, cash_balance):
        self.portfolio = []
        self.cash_balance = cash_balance

    def add_stock(self, stock):
        for pf in self.portfolio:
            if pf['name'] == stock['name']:
                pf['quantity'] += stock['quantity']
                return

        self.portfolio.append(stock)

    def remove_stock(self, stock):
        for pf in self.portfolio:
            if pf['name'] == stock['name'] and pf['quantity'] >= stock['quantity']:
                pf['quantity'] -= stock['quantity']
                if pf['quantity'] == 0:
                    self.portfolio.remove(pf)
                return True
        return False

    def buy_stock(self, stock):
        if stock['price'] * stock['quantity'] > self.cash_balance:
            return False
        else:
            self.add_stock(stock)
            self.cash_balance -= stock['price'] * stock['quantity']
            return True

    def sell_stock(self, stock):
        if self.remove_stock(stock) == False:
            return False
        self.cash_balance += stock['price'] * stock['quantity']
        return True

    def calculate_portfolio_value(self):
        total_value = self.cash_balance
        for stock in self.portfolio:
            total_value += stock['price'] * stock['quantity']
        return total_value

    def get_portfolio_summary(self):
        summary = []
        for stock in self.portfolio:
            value = self.get_stock_value(stock)
            summary.append({"name": stock["name"], "value": value})
        portfolio_value = self.calculate_portfolio_value()
        return portfolio_value, summary

    def get_stock_value(self, stock):
        return stock['price'] * stock['quantity']