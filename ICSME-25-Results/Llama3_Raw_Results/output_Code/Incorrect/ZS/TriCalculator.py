# The class allows to calculate trigonometric values, including cosine, sine, and tangent, using Taylor series approximations.

from math import pi, fabs

class TriCalculator:

    def __init__(self):
        # Initialize the class
        pass

    def cos(self, x):
        """
        Calculate the cos value of the x-degree angle
        :return: float
        """
        # Use the taylor method to calculate the cosine value
        return self.taylor(x, 10)

    def factorial(self, a):
        """
        Calculate the factorial of a
        :return: int
        """
        # Base case for factorial calculation
        if a == 0:
            return 1
        # Recursive case for factorial calculation
        else:
            return a * self.factorial(a-1)

    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :return: float
        """
        # Initialize the sum of the Taylor series
        sum = 0
        # Calculate the Taylor series
        for i in range(n):
            # Calculate the sign of the term
            sign = (-1)**i
            # Calculate the term
            term = (sign * (x/180*pi)**(2*i)) / self.factorial(2*i)
            # Add the term to the sum
            sum += term
        # Return the sum of the Taylor series
        return sum

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :return: float
        """
        # Use the Taylor series expansion for sine
        sum = 0
        for i in range(10):
            # Calculate the sign of the term
            sign = (-1)**i
            # Calculate the term
            term = (sign * (x/180*pi)**(2*i+1)) / self.factorial(2*i+1)
            # Add the term to the sum
            sum += term
        # Return the sum of the Taylor series
        return sum

    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :return: float
        """
        # Calculate the tangent value using the sine and cosine values
        if self.cos(x) == 0:
            # Handle the case where cosine is zero
            return float('inf')
        else:
            return self.sin(x) / self.cos(x)