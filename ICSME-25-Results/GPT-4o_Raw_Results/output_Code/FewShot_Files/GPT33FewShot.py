class DiscountStrategy:
    """
    This is a class that allows to use different discount strategy based on shopping credit or shopping cart in supermarket.
    """

    def __init__(self, customer, cart, promotion=None):
        """
        Initialize the DiscountStrategy with customer information, a cart of items, and an optional promotion.
        :param customer: dict, customer information
        :param cart: list of dicts, a cart of items with details
        :param promotion: function, optional promotion applied to the order
        """
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        """
        Calculate the total cost of items in the cart.
        :return: float, total cost of items
        """
        # Calculate the total price by summing up the price of each item times its quantity
        return sum(item['quantity'] * item['price'] for item in self.cart)

    def due(self):
        """
        Calculate the final amount to be paid after applying the discount.
        :return: float, final amount to be paid
        """
        # Calculate the total cost of the cart
        total = self.total()
        # If a promotion is provided, apply it to the order to get the discount
        if self.promotion:
            discount = self.promotion(self)
        else:
            discount = 0
        # Subtract the discount from the total to get the final due amount
        return total - discount

    @staticmethod
    def FidelityPromo(order):
        """
        Calculate the discount based on the fidelity points of the customer.
        Customers with over 1000 points can enjoy a 5% discount on the entire order.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        """
        # Check if the customer has more than 1000 fidelity points
        if order.customer['fidelity'] > 1000:
            # Return 5% of the total as discount
            return order.total() * 0.05
        return 0

    @staticmethod
    def BulkItemPromo(order):
        """
        Calculate the discount based on bulk item quantity in the order.
        In the same order, if the quantity of a single item reaches 20 or more, each item will enjoy a 10% discount.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        """
        # Calculate discount for items with quantity 20 or more
        discount = 0
        for item in order.cart:
            if item['quantity'] >= 20:
                # 10% discount for each bulk item
                discount += item['quantity'] * item['price'] * 0.1
        return discount

    @staticmethod
    def LargeOrderPromo(order):
        """
        Calculate the discount based on the number of different products in the order.
        If the quantity of different products in the order reaches 10 or more, the entire order will enjoy a 7% discount.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        """
        # Check if there are 10 or more different products in the cart
        if len(order.cart) >= 10:
            # Return 7% of the total as discount
            return order.total() * 0.07
        return 0