class ComplexCalculator:
    def __init__(self):
        pass

    @staticmethod
    def add(c1, c2):
        return c1 + c2

    @staticmethod
    def subtract(c1, c2):
        return c1 - c2

    @staticmethod
    def multiply(c1, c2):
        return c1 * c2

    @staticmethod
    def divide(c1, c2):
        if c2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return c1 / c2