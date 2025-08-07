from math import pi, fabs

class TriCalculator:
    def __init__(self):
        pass

    def cos(self, x):
        return self.taylor(x, 50)

    def factorial(self, a):
        if a == 0:
            return 1
        else:
            return a * self.factorial(a - 1)

    def taylor(self, x, n):
        x = x * pi / 180
        result = 0
        for i in range(n):
            result += ((-1) ** i) * (x ** (2 * i)) / self.factorial(2 * i)
        return result

    def sin(self, x):
        return self.taylor(x - 90, 50)

    def tan(self, x):
        cos_x = self.cos(x)
        if fabs(cos_x) < 1e-10:
            raise ValueError("Tangent is undefined for this angle.")
        return self.sin(x) / cos_x