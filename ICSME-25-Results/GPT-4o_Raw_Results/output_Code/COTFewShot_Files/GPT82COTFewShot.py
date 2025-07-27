class StockPortfolioTracker:
    def __init__(self, cash_balance):
        self.portfolio = []
        self.cash_balance = cash_balance

    def add_stock(self, stock):
        self.portfolio.append(stock)

    def remove_stock(self, stock):
        if stock in self.portfolio:
            self.portfolio.remove(stock)
            return True
        return False

    def buy_stock(self, stock):
        total_cost = stock['price'] * stock['quantity']
        if self.cash_balance >= total_cost:
            self.add_stock(stock)
            self.cash_balance -= total_cost
            return True
        return False

    def sell_stock(self, stock):
        for s in self.portfolio:
            if s['name'] == stock['name'] and s['quantity'] >= stock['quantity']:
                s['quantity'] -= stock['quantity']
                self.cash_balance += stock['price'] * stock['quantity']
                if s['quantity'] == 0:
                    self.portfolio.remove(s)
                return True
        return False

    def calculate_portfolio_value(self):
        total_value = self.cash_balance
        for stock in self.portfolio:
            total_value += stock['price'] * stock['quantity']
        return total_value

    def get_portfolio_summary(self):
        total_value = self.calculate_portfolio_value()
        summary = [{'name': stock['name'], 'value': stock['price'] * stock['quantity']} for stock in self.portfolio]
        return total_value, summary

    def get_stock_value(self, stock):
        return stock['price'] * stock['quantity']