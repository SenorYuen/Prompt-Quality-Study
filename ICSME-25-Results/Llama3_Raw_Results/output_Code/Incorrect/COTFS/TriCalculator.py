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
            return a * self.factorial(a-1)

    def taylor(self, x, n):
        sum = 0
        for i in range(n):
            sign = (-1)**i
            sum += ((x/180*pi)**(2.0*i)) / self.factorial(2*i)
        return sum

    def sin(self, x):
        sum = 0
        for i in range(50):
            sign = (-1)**i
            sum += ((x/180*pi)**(2.0*i+1)) / self.factorial(2*i+1)
        return sum

    def tan(self, x):
        return self.sin(x) / self.cos(x)