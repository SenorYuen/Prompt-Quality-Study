import random

class TwentyFourPointGame:
    def __init__(self):
        self.nums = []

    def _generate_cards(self):
        self.nums = [random.randint(1, 9) for _ in range(4)]

    def get_my_cards(self):
        self._generate_cards()
        return self.nums

    def answer(self, expression):
        try:
            result = eval(expression)
            return result == 24
        except:
            return False

    def evaluate_expression(self, expression):
        return self.answer(expression)