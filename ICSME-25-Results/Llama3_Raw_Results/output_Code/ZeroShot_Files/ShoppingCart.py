class ShoppingCart:
    def __init__(self):
        # Initialize the items representing the shopping list as an empty dictionary
        self.items = {}

    def add_item(self, item, price, quantity=1):
        # Check if the item already exists in the shopping list
        if item in self.items:
            # If the item exists, update its quantity
            self.items[item]['quantity'] += quantity
        else:
            # If the item does not exist, add it to the shopping list
            self.items[item] = {'price': price, 'quantity': quantity}

    def remove_item(self, item, quantity=1):
        # Check if the item exists in the shopping list
        if item in self.items:
            # If the item exists, subtract the specified quantity
            if self.items[item]['quantity'] <= quantity:
                # If the quantity to be removed is greater than or equal to the existing quantity, remove the item from the shopping list
                del self.items[item]
            else:
                # If the quantity to be removed is less than the existing quantity, update the quantity
                self.items[item]['quantity'] -= quantity
        else:
            # If the item does not exist, print an error message
            print(f"Item '{item}' not found in the shopping list.")

    def view_items(self) -> dict:
        # Return the current shopping list items
        return self.items

    def total_price(self) -> float:
        # Initialize the total price to 0
        total = 0
        # Iterate over each item in the shopping list
        for item in self.items:
            # Calculate the total price by multiplying the quantity of each item by its price and adding it to the total
            total += self.items[item]['price'] * self.items[item]['quantity']
        # Return the total price
        return total


# Example usage:
def main():
    cart = ShoppingCart()
    cart.add_item('apple', 1.00, 2)
    cart.add_item('banana', 0.50, 3)
    print(cart.view_items())
    print(f"Total price: ${cart.total_price():.2f}")
    cart.remove_item('apple', 1)
    print(cart.view_items())
    print(f"Total price: ${cart.total_price():.2f}")


if __name__ == "__main__":
    main()