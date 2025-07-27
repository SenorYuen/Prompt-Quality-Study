class BigNumCalculator:
    """
    This is a class that implements big number calculations, including adding, subtracting and multiplying.
    """

    @staticmethod
    def add(num1, num2):
        # Convert input strings to integers
        num1 = int(num1)
        num2 = int(num2)
        
        # Calculate the sum
        result = num1 + num2
        
        # Convert the result back to a string
        return str(result)

    @staticmethod
    def subtract(num1, num2):
        # Convert input strings to integers
        num1 = int(num1)
        num2 = int(num2)
        
        # Calculate the difference
        result = num1 - num2
        
        # Convert the result back to a string
        return str(result)

    @staticmethod
    def multiply(num1, num2):
        # Convert input strings to integers
        num1 = int(num1)
        num2 = int(num2)
        
        # Calculate the product
        result = num1 * num2
        
        # Convert the result back to a string
        return str(result)