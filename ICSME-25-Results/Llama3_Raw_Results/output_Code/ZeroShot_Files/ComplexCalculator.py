# This is a class that implements addition, subtraction, multiplication, and division operations for complex numbers.

class ComplexCalculator:

    def __init__(self):
        # Initialize an empty constructor as no instance variables are required
        pass

    @staticmethod
    def add(c1, c2):
        """
        Adds two complex numbers.
        :return: The sum of the two complex numbers, complex.
        """
        # Extract real and imaginary parts of the complex numbers
        real1, imag1 = c1.real, c1.imag
        real2, imag2 = c2.real, c2.imag
        
        # Calculate the sum of real and imaginary parts separately
        real_sum = real1 + real2
        imag_sum = imag1 + imag2
        
        # Return the sum as a complex number
        return complex(real_sum, imag_sum)

    @staticmethod
    def subtract(c1, c2):
        """
        Subtracts two complex numbers.
        :return: The difference of the two complex numbers, complex.
        """
        # Extract real and imaginary parts of the complex numbers
        real1, imag1 = c1.real, c1.imag
        real2, imag2 = c2.real, c2.imag
        
        # Calculate the difference of real and imaginary parts separately
        real_diff = real1 - real2
        imag_diff = imag1 - imag2
        
        # Return the difference as a complex number
        return complex(real_diff, imag_diff)

    @staticmethod
    def multiply(c1, c2):
        """
        Multiplies two complex numbers.
        :return: The product of the two complex numbers, complex.
        """
        # Extract real and imaginary parts of the complex numbers
        real1, imag1 = c1.real, c1.imag
        real2, imag2 = c2.real, c2.imag
        
        # Calculate the product using the formula (a+bi)*(c+di) = (ac-bd) + (ad+bc)i
        real_product = real1 * real2 - imag1 * imag2
        imag_product = real1 * imag2 + real2 * imag1
        
        # Return the product as a complex number
        return complex(real_product, imag_product)

    @staticmethod
    def divide(c1, c2):
        """
        Divides two complex numbers.
        :return: The quotient of the two complex numbers, complex.
        """
        # Check for division by zero
        if c2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        # Extract real and imaginary parts of the complex numbers
        real1, imag1 = c1.real, c1.imag
        real2, imag2 = c2.real, c2.imag
        
        # Calculate the magnitude of the denominator
        magnitude = real2 ** 2 + imag2 ** 2
        
        # Calculate the quotient using the formula (a+bi)/(c+di) = ((ac+bd)/magnitude) + ((bc-ad)/magnitude)i
        real_quotient = (real1 * real2 + imag1 * imag2) / magnitude
        imag_quotient = (imag1 * real2 - real1 * imag2) / magnitude
        
        # Return the quotient as a complex number
        return complex(real_quotient, imag_quotient)


# Example usage:
if __name__ == "__main__":
    c1 = complex(3, 4)
    c2 = complex(1, 2)
    
    print("Addition:", ComplexCalculator.add(c1, c2))
    print("Subtraction:", ComplexCalculator.subtract(c1, c2))
    print("Multiplication:", ComplexCalculator.multiply(c1, c2))
    print("Division:", ComplexCalculator.divide(c1, c2))