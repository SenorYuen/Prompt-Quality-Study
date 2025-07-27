class ComplexCalculator:
    """
    This is a class that implements addition, subtraction, multiplication, and division operations for complex numbers.
    """

    def __init__(self):
        pass

    # Method to add two complex numbers
    @staticmethod
    def add(c1, c2):
        # Simply add the real and imaginary parts of the two complex numbers
        return c1 + c2

    # Method to subtract two complex numbers
    @staticmethod
    def subtract(c1, c2):
        # Simply subtract the real and imaginary parts of the two complex numbers
        return c1 - c2

    # Method to multiply two complex numbers
    @staticmethod
    def multiply(c1, c2):
        # Use the formula for complex multiplication: (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        # However, Python's built-in complex number support handles this automatically
        return c1 * c2

    # Method to divide two complex numbers
    @staticmethod
    def divide(c1, c2):
        # Use the formula for complex division: (a + bi)/(c + di) = ((ac + bd) / (c^2 + d^2)) + ((bc - ad) / (c^2 + d^2))i
        # However, Python's built-in complex number support handles this automatically
        if c2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return c1 / c2