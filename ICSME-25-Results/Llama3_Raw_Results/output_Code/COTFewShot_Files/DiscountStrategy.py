class DiscountStrategy:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion
        self.total()

    def total(self):
        total_cost = sum(item['quantity'] * item['price'] for item in self.cart)
        return total_cost

    def due(self):
        total_cost = self.total()
        if self.promotion:
            discount = self.promotion(self)
            return total_cost - discount
        else:
            return total_cost

    @staticmethod
    def FidelityPromo(order):
        if order.customer['fidelity'] > 1000:
            return order.total() * 0.05
        else:
            return 0.0

    @staticmethod
    def BulkItemPromo(order):
        discount = 0.0
        for item in order.cart:
            if item['quantity'] >= 20:
                discount += item['quantity'] * item['price'] * 0.10
        return discount

    @staticmethod
    def LargeOrderPromo(order):
        unique_products = len(set(item['product'] for item in order.cart))
        if unique_products >= 10:
            return order.total() * 0.07
        else:
            return 0.0