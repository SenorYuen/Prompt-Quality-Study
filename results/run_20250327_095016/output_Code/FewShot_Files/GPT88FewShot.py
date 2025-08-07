from math import pi, fabs

class TriCalculator:
    """
    The class allows to calculate trigonometric values, including cosine, sine, and tangent, using Taylor series approximations.
    """

    def __init__(self):
        pass

    def cos(self, x):
        """
        Calculate the cos value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.cos(60)
        0.5
        """
        # Convert degrees to radians
        x_rad = x * pi / 180
        # Use the Taylor series approximation
        return self.taylor(x_rad, 50)

    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        >>> tricalculator.factorial(5)
        120
        """
        if a == 0:
            return 1
        else:
            result = 1
            for i in range(1, a + 1):
                result *= i
            return result

    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        >>> tricalculator.taylor(60, 50)
        0.5000000000000001
        """
        # Initialize the Taylor series sum
        sum = 0
        # Calculate the Taylor series up to n terms
        for i in range(n):
            term = ((-1) ** i) * (x ** (2 * i)) / self.factorial(2 * i)
            sum += term
        return sum

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
        # Convert degrees to radians
        x_rad = x * pi / 180
        # Use the Taylor series approximation for sine
        sum = 0
        for i in range(50):
            term = ((-1) ** i) * (x_rad ** (2 * i + 1)) / self.factorial(2 * i + 1)
            sum += term
        return sum

    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
        # Use the sine and cosine functions to calculate tangent
        cos_val = self.cos(x)
        if cos_val == 0:
            raise ValueError("Tangent undefined for this angle.")
        sin_val = self.sin(x)
        return sin_val / cos_val