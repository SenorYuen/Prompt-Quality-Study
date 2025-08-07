from math import pi, fabs

class TriCalculator:
    def __init__(self):
        pass

    def factorial(self, a):
        if a == 0 or a == 1:
            return 1
        else:
            result = 1
            for i in range(2, a + 1):
                result *= i
            return result

    def taylor(self, x, n):
        x_rad = x * pi / 180
        result = 0
        for i in range(n + 1):
            term = ((-1) ** i) * (x_rad ** (2 * i)) / self.factorial(2 * i)
            result += term
        return result

    def cos(self, x):
        return self.taylor(x, 50)

    def sin(self, x):
        x_rad = x * pi / 180
        result = 0
        for i in range(50):
            term = ((-1) ** i) * (x_rad ** (2 * i + 1)) / self.factorial(2 * i + 1)
            result += term
        return result

    def tan(self, x):
        cos_value = self.cos(x)
        sin_value = self.sin(x)
        if fabs(cos_value) < 1e-10:
            raise ValueError("Tangent undefined for this angle.")
        return sin_value / cos_value