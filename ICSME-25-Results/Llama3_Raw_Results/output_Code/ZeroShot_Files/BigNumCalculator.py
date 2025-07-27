# This is a class that implements big number calculations, including adding, subtracting and multiplying.

class BigNumCalculator:
    @staticmethod
    def add(num1, num2):
        """
        Adds two big numbers.
        :return: The sum of the two numbers,str.
        """
        # Convert input numbers to integers, add them, and convert back to string
        return str(int(num1) + int(num2))

    @staticmethod
    def subtract(num1, num2):
        """
        Subtracts two big numbers.
        :return: The difference of the two numbers,str.
        """
        # Convert input numbers to integers, subtract them, and convert back to string
        # Check if num1 is greater than num2 to avoid negative result
        if int(num1) >= int(num2):
            return str(int(num1) - int(num2))
        else:
            return '-' + str(int(num2) - int(num1))

    @staticmethod
    def multiply(num1, num2):
        """
        Multiplies two big numbers.
        :return: The product of the two numbers,str.
        """
        # Convert input numbers to integers, multiply them, and convert back to string
        return str(int(num1) * int(num2))


# Example usage:
print(BigNumCalculator.add('12345678901234567890', '98765432109876543210'))
print(BigNumCalculator.subtract('12345678901234567890', '98765432109876543210'))
print(BigNumCalculator.multiply('12345678901234567890', '98765432109876543210'))