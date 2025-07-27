import random

class TwentyFourPointGame:
    def __init__(self) -> None:
        # Initialize an empty list to store the numbers
        self.nums = []

    def _generate_cards(self):
        # Generate four random numbers between 1 and 9
        self.nums = random.sample(range(1, 10), 4)

    def get_my_cards(self):
        # Generate the cards if they haven't been generated yet
        if not self.nums:
            self._generate_cards()
        # Return a list of the four numbers
        return self.nums

    def answer(self, expression):
        # Replace the numbers in the expression with the actual numbers
        for i, num in enumerate(self.nums):
            expression = expression.replace(f'num{i+1}', str(num))
        # Evaluate the expression and check if the result is 24
        return self.evaluate_expression(expression)

    def evaluate_expression(self, expression):
        # Try to evaluate the expression
        try:
            # Evaluate the expression
            result = eval(expression)
            # Check if the result is 24
            return result == 24
        except Exception as e:
            # If an error occurs during evaluation, return False
            print(f"Error evaluating expression: {e}")
            return False

# Example usage:
game = TwentyFourPointGame()
cards = game.get_my_cards()
print(f"Your cards are: {cards}")
expression = input("Enter a mathematical expression using the numbers (e.g., 'num1 + num2 * num3 - num4'): ")
print(f"Is the expression equal to 24? {game.answer(expression)}")