class DiscountStrategy:
    def __init__(self, customer, cart, promotion=None):
        """
        Initialize the DiscountStrategy with customer information, a cart of items, and an optional promotion.
        :param customer: dict, contains customer information including fidelity points
        :param cart: list of tuples, each tuple contains (product, quantity, price)
        :param promotion: function, a promotion function to apply
        """
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        """
        Calculate the total cost of items in the cart.
        :return: float, total cost of items
        """
        return sum(item[1] * item[2] for item in self.cart)

    def due(self):
        """
        Calculate the final amount to be paid after applying the discount.
        :return: float, final amount to be paid
        """
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    @staticmethod
    def FidelityPromo(order):
        """
        Calculate the discount based on the fidelity points of the customer.
        Customers with over 1000 points can enjoy a 5% discount on the entire order.
        :param order: DiscountStrategy instance
        :return: float, discount amount
        """
        if order.customer.get('fidelity', 0) > 1000:
            return order.total() * 0.05
        return 0

    @staticmethod
    def BulkItemPromo(order):
        """
        Calculate the discount based on bulk item quantity in the order.
        In the same order, if the quantity of a single item reaches 20 or more, each item will enjoy a 10% discount.
        :param order: DiscountStrategy instance
        :return: float, discount amount
        """
        discount = 0
        for item in order.cart:
            if item[1] >= 20:
                discount += item[1] * item[2] * 0.10
        return discount

    @staticmethod
    def LargeOrderPromo(order):
        """
        Calculate the discount based on the number of different products in the order.
        If the quantity of different products in the order reaches 10 or more, the entire order will enjoy a 7% discount.
        :param order: DiscountStrategy instance
        :return: float, discount amount
        """
        if len(order.cart) >= 10:
            return order.total() * 0.07
        return 0