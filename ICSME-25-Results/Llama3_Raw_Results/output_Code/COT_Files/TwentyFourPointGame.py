import random

class TwentyFourPointGame:
    def __init__(self):
        self.nums = []

    def _generate_cards(self):
        self.nums = random.sample(range(1, 10), 4)

    def get_my_cards(self):
        self._generate_cards()
        return self.nums

    def evaluate_expression(self, expression):
        try:
            result = eval(expression)
            return result == 24
        except Exception:
            return False

    def answer(self, expression):
        return self.evaluate_expression(expression)