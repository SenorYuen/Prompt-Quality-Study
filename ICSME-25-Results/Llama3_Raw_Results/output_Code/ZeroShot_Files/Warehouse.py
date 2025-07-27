class Warehouse:
    def __init__(self):
        """
        Initialize two fields.
        """
        # Dictionary to store products with product ID as key
        self.inventory = {}  
        # Dictionary to store orders with order ID as key
        self.orders = {}  

    def add_product(self, product_id, name, quantity):
        """
        Add product to inventory and plus the quantity if it has existed in inventory.
        Or just add new product to dict otherwise.
        """
        # Check if product already exists in inventory
        if product_id in self.inventory:
            # If product exists, update its quantity
            self.inventory[product_id]['quantity'] += quantity
        else:
            # If product does not exist, add it to inventory
            self.inventory[product_id] = {'name': name, 'quantity': quantity}

    def update_product_quantity(self, product_id, quantity):
        """
        According to product_id, add the quantity to the corresponding product in inventory.
        """
        # Check if product exists in inventory
        if product_id in self.inventory:
            # Update product quantity
            self.inventory[product_id]['quantity'] += quantity
        else:
            # Raise error if product does not exist
            raise ValueError("Product does not exist in inventory")

    def get_product_quantity(self, product_id):
        """
        Get the quantity of specific product by product_id.
        :return: if the product_id is in inventory then return the corresponding quantity,
                or False otherwise.
        """
        # Check if product exists in inventory
        if product_id in self.inventory:
            # Return product quantity
            return self.inventory[product_id]['quantity']
        else:
            # Return False if product does not exist
            return False

    def create_order(self, order_id, product_id, quantity):
        """
        Create a order which includes the infomation of product, like id and quantity.
        And put the new order into self.orders.
        The default value of status is 'Shipped'.
        :return False: only if product_id is not in inventory or the quantity is not adequate
        """
        # Check if product exists in inventory and quantity is adequate
        if product_id in self.inventory and self.inventory[product_id]['quantity'] >= quantity:
            # Create new order
            self.orders[order_id] = {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}
            # Update product quantity
            self.inventory[product_id]['quantity'] -= quantity
            # Return True to indicate successful order creation
            return True
        else:
            # Return False if product does not exist or quantity is not adequate
            return False

    def change_order_status(self, order_id, status):
        """
        Change the status of order if the input order_id is in self.orders.
        :return False: only if the order_id is not in self.orders
        """
        # Check if order exists
        if order_id in self.orders:
            # Update order status
            self.orders[order_id]['status'] = status
            # Return True to indicate successful status update
            return True
        else:
            # Return False if order does not exist
            return False

    def track_order(self, order_id):
        """
        Get the status of specific order.
        :return False: only if the order_id is not in self.orders.
        """
        # Check if order exists
        if order_id in self.orders:
            # Return order status
            return self.orders[order_id]['status']
        else:
            # Return False if order does not exist
            return False


# Example usage:
warehouse = Warehouse()
warehouse.add_product('P1', 'Product 1', 100)
print(warehouse.get_product_quantity('P1'))  # Output: 100
warehouse.create_order('O1', 'P1', 50)
print(warehouse.track_order('O1'))  # Output: Shipped
warehouse.change_order_status('O1', 'Delivered')
print(warehouse.track_order('O1'))  # Output: Delivered