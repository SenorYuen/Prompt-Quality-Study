import random

class TwentyFourPointGame:
    """
    This is a game of twenty-four points, which provides to generate four numbers and check whether player's expression is equal to 24.
    """

    def __init__(self) -> None:
        # Initialize an empty list to store the generated numbers
        self.nums = []

    def _generate_cards(self):
        # Generate four random numbers between 1 and 9
        self.nums = random.sample(range(1, 10), 4)

    def get_my_cards(self):
        # Generate the numbers if they haven't been generated yet
        if not self.nums:
            self._generate_cards()
        # Return the list of generated numbers
        return self.nums

    def answer(self, expression):
        # Replace the numbers in the expression with the actual numbers
        for i, num in enumerate(self.nums):
            expression = expression.replace(str(i+1), str(num))
        # Evaluate the expression
        return self.evaluate_expression(expression)

    def evaluate_expression(self, expression):
        # Try to evaluate the expression
        try:
            # Use eval to evaluate the expression
            result = eval(expression)
            # Check if the result is 24
            return result == 24
        except:
            # If an error occurs, return False
            return False