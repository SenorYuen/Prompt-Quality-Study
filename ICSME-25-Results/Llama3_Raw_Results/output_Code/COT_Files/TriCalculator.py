from math import pi, fabs

class TriCalculator:
    def __init__(self):
        pass

    def cos(self, x):
        return self.taylor(x, 50)

    def factorial(self, a):
        result = 1
        for i in range(1, a + 1):
            result *= i
        return result

    def taylor(self, x, n):
        result = 0
        for i in range(n):
            sign = (-1) ** i
            result += ((x / 180 * pi) ** (2 * i)) / self.factorial(2 * i) * sign
        return result

    def sin(self, x):
        result = 0
        for i in range(50):
            sign = (-1) ** i
            result += ((x / 180 * pi) ** (2 * i + 1)) / self.factorial(2 * i + 1) * sign
        return result

    def tan(self, x):
        return self.sin(x) / self.cos(x)