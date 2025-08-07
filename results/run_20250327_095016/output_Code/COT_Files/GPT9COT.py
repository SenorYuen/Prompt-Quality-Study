class BigNumCalculator:

    @staticmethod
    def add(num1, num2):
        # Convert the input strings to integers, perform addition, and convert the result back to string
        return str(int(num1) + int(num2))

    @staticmethod
    def subtract(num1, num2):
        # Convert the input strings to integers, perform subtraction, and convert the result back to string
        return str(int(num1) - int(num2))

    @staticmethod
    def multiply(num1, num2):
        # Convert the input strings to integers, perform multiplication, and convert the result back to string
        return str(int(num1) * int(num2))