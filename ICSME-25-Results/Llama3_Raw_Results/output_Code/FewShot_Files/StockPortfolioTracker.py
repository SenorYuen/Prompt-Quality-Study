class StockPortfolioTracker:
    """
    This is a class as StockPortfolioTracker that allows to add stocks, remove stocks, buy stocks, sell stocks, calculate the total value of the portfolio, and obtain a summary of the portfolio.
    """

    def __init__(self, cash_balance):
        """
        Initialize the StockPortfolioTracker class with a cash balance and an empty portfolio.
        """
        self.portfolio = []
        self.cash_balance = cash_balance

    def add_stock(self, stock):
        # Add a stock to the portfolio
        self.portfolio.append(stock)

    def remove_stock(self, stock):
        # Remove a stock from the portfolio
        for s in self.portfolio:
            if s['name'] == stock['name'] and s['price'] == stock['price'] and s['quantity'] == stock['quantity']:
                self.portfolio.remove(s)
                return True
        return False

    def buy_stock(self, stock):
        # Buy a stock and add it to the portfolio
        total_cost = stock['price'] * stock['quantity']
        if self.cash_balance >= total_cost:
            self.cash_balance -= total_cost
            self.add_stock(stock)
            return True
        return False

    def sell_stock(self, stock):
        # Sell a stock and remove it from the portfolio and add the cash to the cash balance
        for s in self.portfolio:
            if s['name'] == stock['name'] and s['price'] == stock['price'] and s['quantity'] <= stock['quantity']:
                self.cash_balance += stock['price'] * stock['quantity']
                self.portfolio.remove(s)
                return True
        return False

    def calculate_portfolio_value(self):
        # Calculate the total value of the portfolio
        total_value = self.cash_balance
        for stock in self.portfolio:
            total_value += stock['price'] * stock['quantity']
        return total_value

    def get_portfolio_summary(self):
        # Get a summary of the portfolio
        total_value = self.calculate_portfolio_value()
        stock_values = []
        for stock in self.portfolio:
            stock_value = stock['price'] * stock['quantity']
            stock_values.append({'name': stock['name'], 'value': stock_value})
        return (total_value, stock_values)

    def get_stock_value(self, stock):
        # Get the value of a stock
        return stock['price'] * stock['quantity']