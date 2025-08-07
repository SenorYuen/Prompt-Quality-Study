class BigNumCalculator:
    @staticmethod
    def add(num1, num2):
        """
        Adds two big numbers.
        :return: The sum of the two numbers, str.
        """
        # Convert the input strings to integers, add them, and convert the result back to a string
        return str(int(num1) + int(num2))

    @staticmethod
    def subtract(num1, num2):
        """
        Subtracts two big numbers.
        :return: The difference of the two numbers, str.
        """
        # Convert the input strings to integers, subtract them, and convert the result back to a string
        return str(int(num1) - int(num2))

    @staticmethod
    def multiply(num1, num2):
        """
        Multiplies two big numbers.
        :return: The product of the two numbers, str.
        """
        # Convert the input strings to integers, multiply them, and convert the result back to a string
        return str(int(num1) * int(num2))