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
        self.total_cost = self.total()  # calculate total cost when initializing

    def total(self):
        """
        Calculate the total cost of items in the cart.
        :return: float, total cost of items
        """
        # calculate total cost by summing up the cost of each item in the cart
        total_cost = sum(item['quantity'] * item['price'] for item in self.cart)
        return total_cost

    def due(self):
        """
        Calculate the final amount to be paid after applying the discount.
        :return: float, final amount to be paid
        """
        # calculate the final amount by applying the discount to the total cost
        if self.promotion:
            discount = self.promotion(self)
            return self.total_cost - discount
        else:
            return self.total_cost

    @staticmethod
    def FidelityPromo(order):
        """
        Calculate the discount based on the fidelity points of the customer.
        Customers with over 1000 points can enjoy a 5% discount on the entire order.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        """
        # check if the customer has over 1000 fidelity points
        if order.customer['fidelity'] > 1000:
            # calculate the discount as 5% of the total cost
            discount = order.total_cost * 0.05
            return discount
        else:
            return 0.0

    @staticmethod
    def BulkItemPromo(order):
        """
        Calculate the discount based on bulk item quantity in the order.
        In the same order, if the quantity of a single item reaches 20 or more, each item will enjoy a 10% discount.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        """
        # initialize the discount amount
        discount = 0.0
        # iterate over each item in the cart
        for item in order.cart:
            # check if the quantity of the item is 20 or more
            if item['quantity'] >= 20:
                # calculate the discount for the item as 10% of the item's cost
                item_discount = item['quantity'] * item['price'] * 0.1
                # add the item's discount to the total discount
                discount += item_discount
        return discount

    @staticmethod
    def LargeOrderPromo(order):
        """
        Calculate the discount based on the number of different products in the order.
        If the quantity of different products in the order reaches 10 or more, the entire order will enjoy a 7% discount.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        """
        # get the number of different products in the order
        num_products = len(set(item['product'] for item in order.cart))
        # check if the number of products is 10 or more
        if num_products >= 10:
            # calculate the discount as 7% of the total cost
            discount = order.total_cost * 0.07
            return discount
        else:
            return 0.0