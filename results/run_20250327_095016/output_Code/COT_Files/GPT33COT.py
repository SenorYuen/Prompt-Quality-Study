class DiscountStrategy:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion
        self.total()

    def total(self):
        return sum(item['quantity'] * item['price'] for item in self.cart)

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    @staticmethod
    def FidelityPromo(order):
        return order.total() * 0.05 if order.customer['fidelity'] > 1000 else 0

    @staticmethod
    def BulkItemPromo(order):
        discount = 0
        for item in order.cart:
            if item['quantity'] >= 20:
                discount += item['quantity'] * item['price'] * 0.1
        return discount

    @staticmethod
    def LargeOrderPromo(order):
        distinct_items = {item['product'] for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0