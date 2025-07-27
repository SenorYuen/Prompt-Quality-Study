class ComplexCalculator:

    def __init__(self):
        pass

    @staticmethod
    def add(c1, c2):
        """
        Adds two complex numbers.
        :return: The sum of the two complex numbers, complex.
        """
        # Use complex number addition: (a+bi) + (c+di) = (a+c) + (b+d)i
        return c1 + c2

    @staticmethod
    def subtract(c1, c2):
        """
        Subtracts two complex numbers.
        :return: The difference of the two complex numbers, complex.
        """
        # Use complex number subtraction: (a+bi) - (c+di) = (a-c) + (b-d)i
        return c1 - c2

    @staticmethod
    def multiply(c1, c2):
        """
        Multiplies two complex numbers.
        :return: The product of the two complex numbers, complex.
        """
        # Use complex number multiplication: (a+bi)(c+di) = (ac-bd) + (ad+bc)i
        return c1 * c2

    @staticmethod
    def divide(c1, c2):
        """
        Divides two complex numbers.
        :return: The quotient of the two complex numbers, complex.
        """
        # Use complex number division: (a+bi)/(c+di) = [(ac+bd) + (bc-ad)i] / (c^2 + d^2)
        if c2 == 0:
            raise ValueError("Cannot divide by zero complex number")
        return c1 / c2