class DiscountStrategy:
    def __init__(self, customer, cart, promotion=None):
        # Initialize the DiscountStrategy with customer information, a cart of items, and an optional promotion.
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        # Calculate the total cost of items in the cart.
        total_cost = sum(item['price'] * item['quantity'] for item in self.cart)
        return total_cost

    def due(self):
        # Calculate the final amount to be paid after applying the discount.
        total_cost = self.total()
        discount = 0
        if self.promotion == 'FidelityPromo':
            discount = self.FidelityPromo(self.cart)
        elif self.promotion == 'BulkItemPromo':
            discount = self.BulkItemPromo(self.cart)
        elif self.promotion == 'LargeOrderPromo':
            discount = self.LargeOrderPromo(self.cart)
        final_amount = total_cost - discount
        return final_amount

    @staticmethod
    def FidelityPromo(order):
        # Calculate the discount based on the fidelity points of the customer.
        # Customers with over 1000 points can enjoy a 5% discount on the entire order.
        total_cost = sum(item['price'] * item['quantity'] for item in order)
        if order[0]['customer_points'] > 1000:
            discount = total_cost * 0.05
        else:
            discount = 0
        return discount

    @staticmethod
    def BulkItemPromo(order):
        # Calculate the discount based on bulk item quantity in the order.
        # In the same order, if the quantity of a single item reaches 20 or more, each item will enjoy a 10% discount.
        discount = 0
        for item in order:
            if item['quantity'] >= 20:
                discount += item['price'] * item['quantity'] * 0.1
        return discount

    @staticmethod
    def LargeOrderPromo(order):
        # Calculate the discount based on the number of different products in the order.
        # If the quantity of different products in the order reaches 10 or more, the entire order will enjoy a 7% discount.
        unique_items = len(set(item['product_id'] for item in order))
        total_cost = sum(item['price'] * item['quantity'] for item in order)
        if unique_items >= 10:
            discount = total_cost * 0.07
        else:
            discount = 0
        return discount

# Example usage:
class Customer:
    def __init__(self, customer_points):
        self.customer_points = customer_points

class Item:
    def __init__(self, product_id, price, quantity):
        self.product_id = product_id
        self.price = price
        self.quantity = quantity

customer = Customer(1200)
cart = [
    {'product_id': 1, 'price': 10, 'quantity': 5, 'customer_points': customer.customer_points},
    {'product_id': 2, 'price': 20, 'quantity': 25, 'customer_points': customer.customer_points},
    {'product_id': 3, 'price': 30, 'quantity': 1, 'customer_points': customer.customer_points},
]

discount_strategy = DiscountStrategy(customer, cart, 'FidelityPromo')
print(discount_strategy.due())

discount_strategy = DiscountStrategy(customer, cart, 'BulkItemPromo')
print(discount_strategy.due())

discount_strategy = DiscountStrategy(customer, cart, 'LargeOrderPromo')
print(discount_strategy.due())