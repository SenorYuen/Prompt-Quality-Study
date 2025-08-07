from math import pi, fabs

class TriCalculator:

    def __init__(self):
        pass

    def cos(self, x):
        """
        Calculate the cos value of the x-degree angle using Taylor series
        :return: float
        """
        # Convert degree to radians
        x_rad = x * pi / 180
        # Use Taylor series with 10 terms for approximation
        return self.taylor(x_rad, 10)

    def factorial(self, a):
        """
        Calculate the factorial of a
        :return: int
        """
        if a == 0:
            return 1
        result = 1
        for i in range(1, a + 1):
            result *= i
        return result

    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos(x)
        :return: float
        """
        cos_approx = 0
        for i in range(n):
            # Calculate each term in the Taylor series for cosine
            term = ((-1) ** i) * (x ** (2 * i)) / self.factorial(2 * i)
            cos_approx += term
        return cos_approx

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle using Taylor series
        :return: float
        """
        # Convert degree to radians
        x_rad = x * pi / 180
        sin_approx = 0
        # Use Taylor series with 10 terms for approximation
        for i in range(10):
            # Calculate each term in the Taylor series for sine
            term = ((-1) ** i) * (x_rad ** (2 * i + 1)) / self.factorial(2 * i + 1)
            sin_approx += term
        return sin_approx

    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :return: float
        """
        # Calculate tan as sin/cos
        cos_value = self.cos(x)
        if fabs(cos_value) < 1e-10:
            raise ValueError("Tangent undefined for this angle as cosine is zero.")
        sin_value = self.sin(x)
        return sin_value / cos_value