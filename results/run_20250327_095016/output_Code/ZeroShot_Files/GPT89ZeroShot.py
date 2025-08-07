import random

class TwentyFourPointGame:
    def __init__(self) -> None:
        self.nums = []

    def _generate_cards(self):
        """
        Generate random numbers between 1 and 9 for the cards.
        """
        self.nums = [random.randint(1, 9) for _ in range(4)]

    def get_my_cards(self):
        """
        Get a list of four random numbers between 1 and 9 representing the player's cards.
        :return: list of integers, representing the player's cards
        """
        if not self.nums:
            self._generate_cards()
        return self.nums

    def answer(self, expression):
        """
        Check if a given mathematical expression using the cards can evaluate to 24.
        :param expression: str, the mathematical expression to evaluate
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        # Ensure the expression only uses the numbers from the generated cards
        card_counts = {num: self.nums.count(num) for num in self.nums}
        try:
            # Evaluate the expression
            result = eval(expression)
            # Check if the result is 24
            if result == 24:
                # Validate that used numbers are from the generated cards
                used_numbers = [int(char) for char in expression if char.isdigit()]
                used_counts = {num: used_numbers.count(num) for num in used_numbers}
                for num, count in used_counts.items():
                    if count > card_counts.get(num, 0):
                        return False
                return True
            return False
        except (SyntaxError, NameError, ZeroDivisionError):
            return False

    def evaluate_expression(self, expression):
        """
        Evaluate a mathematical expression and check if the result is 24.
        :param expression: str, the mathematical expression to evaluate
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        return self.answer(expression)