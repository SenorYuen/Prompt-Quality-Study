class Stock:
    def __init__(self, name, price, quantity):
        """
        Initialize the Stock class with a name, price, and quantity.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

class StockPortfolioTracker:
    def __init__(self, cash_balance):
        """
        Initialize the StockPortfolioTracker class with a cash balance and an empty portfolio.
        """
        # Initialize cash balance
        self.cash_balance = cash_balance
        # Initialize an empty portfolio
        self.portfolio = {}

    def add_stock(self, stock):
        """
        Add a stock to the portfolio.
        """
        # Check if the stock is already in the portfolio
        if stock.name in self.portfolio:
            # If the stock is already in the portfolio, increase its quantity
            self.portfolio[stock.name].quantity += stock.quantity
        else:
            # If the stock is not in the portfolio, add it
            self.portfolio[stock.name] = stock

    def remove_stock(self, stock):
        """
        Remove a stock from the portfolio.
        """
        # Check if the stock is in the portfolio
        if stock.name in self.portfolio:
            # If the stock is in the portfolio, remove it
            del self.portfolio[stock.name]
        else:
            # If the stock is not in the portfolio, print an error message
            print("Stock not found in portfolio.")

    def buy_stock(self, stock):
        """
        Buy a stock and add it to the portfolio.
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        """
        # Calculate the total cost of the stock
        total_cost = stock.price * stock.quantity
        # Check if the cash balance is enough to buy the stock
        if self.cash_balance >= total_cost:
            # If the cash balance is enough, subtract the total cost from the cash balance
            self.cash_balance -= total_cost
            # Add the stock to the portfolio
            self.add_stock(stock)
            # Return True to indicate that the stock was bought successfully
            return True
        else:
            # If the cash balance is not enough, return False
            return False

    def sell_stock(self, stock):
        """
        Sell a stock and remove it from the portfolio and add the cash to the cash balance.
        :return: True if the stock was sold successfully, False if the quantity of the stock is not enough.
        """
        # Check if the stock is in the portfolio
        if stock.name in self.portfolio:
            # If the stock is in the portfolio, check if the quantity is enough
            if self.portfolio[stock.name].quantity >= stock.quantity:
                # If the quantity is enough, subtract the quantity from the portfolio
                self.portfolio[stock.name].quantity -= stock.quantity
                # Calculate the total revenue from selling the stock
                total_revenue = stock.price * stock.quantity
                # Add the total revenue to the cash balance
                self.cash_balance += total_revenue
                # If the quantity of the stock in the portfolio is 0, remove it from the portfolio
                if self.portfolio[stock.name].quantity == 0:
                    self.remove_stock(stock)
                # Return True to indicate that the stock was sold successfully
                return True
            else:
                # If the quantity is not enough, return False
                return False
        else:
            # If the stock is not in the portfolio, return False
            return False

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio.
        :return: the total value of the portfolio, float.
        """
        # Initialize the total value of the portfolio to 0
        total_value = self.cash_balance
        # Iterate over each stock in the portfolio
        for stock in self.portfolio.values():
            # Add the value of the stock to the total value
            total_value += stock.price * stock.quantity
        # Return the total value of the portfolio
        return total_value

    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        """
        # Initialize a list to store the summary of each stock
        stock_summaries = []
        # Iterate over each stock in the portfolio
        for stock in self.portfolio.values():
            # Calculate the value of the stock
            stock_value = stock.price * stock.quantity
            # Add a dictionary with the name and value of the stock to the list
            stock_summaries.append({"name": stock.name, "value": stock_value})
        # Calculate the total value of the portfolio
        total_value = self.calculate_portfolio_value()
        # Return a tuple of the total value and the list of stock summaries
        return (total_value, stock_summaries)

    def get_stock_value(self, stock):
        """
        Get the value of a stock.
        :return: the value of the stock, float.
        """
        # Check if the stock is in the portfolio
        if stock.name in self.portfolio:
            # If the stock is in the portfolio, return its value
            return self.portfolio[stock.name].price * self.portfolio[stock.name].quantity
        else:
            # If the stock is not in the portfolio, return 0
            return 0

# Example usage
if __name__ == "__main__":
    # Create a new StockPortfolioTracker with a cash balance of 1000
    tracker = StockPortfolioTracker(1000)
    # Create a new stock with a name, price, and quantity
    stock1 = Stock("Apple", 100, 10)
    stock2 = Stock("Google", 500, 5)
    # Buy the stocks
    tracker.buy_stock(stock1)
    tracker.buy_stock(stock2)
    # Print the portfolio summary
    print(tracker.get_portfolio_summary())
    # Sell a stock
    tracker.sell_stock(stock1)
    # Print the portfolio summary again
    print(tracker.get_portfolio_summary())