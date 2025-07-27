from math import pi, fabs

class TriCalculator:
    """
    The class allows to calculate trigonometric values, including cosine, sine, and tangent, using Taylor series approximations.
    """

    def __init__(self):
        pass

    # Calculate the cos value of the x-degree angle using Taylor series approximation
    def cos(self, x):
        """
        Calculate the cos value of the x-degree angle
        :param x:float
        :return:float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.cos(60)
        0.5
        """
        return self.taylor(x, 50)  # Use 50 terms for Taylor series approximation

    # Calculate the factorial of a number
    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        >>> tricalculator.factorial(5)
        120
        """
        result = 1
        for i in range(1, a + 1):
            result *= i
        return result

    # Calculate the n-order Taylor expansion value of cos (x/180 * pi)
    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        >>> tricalculator.taylor(60, 50)
        0.5000000000000001
        """
        result = 0
        for i in range(n):
            sign = (-1) ** i
            result += ((x / 180 * pi) ** (2 * i)) / self.factorial(2 * i) * sign
        return result

    # Calculate the sin value of the x-degree angle using Taylor series approximation
    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
        result = 0
        for i in range(50):  # Use 50 terms for Taylor series approximation
            sign = (-1) ** i
            result += ((x / 180 * pi) ** (2 * i + 1)) / self.factorial(2 * i + 1) * sign
        return result

    # Calculate the tan value of the x-degree angle using sin and cos values
    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
        return self.sin(x) / self.cos(x)