class BigNumCalculator:
    @staticmethod
    def add(num1, num2):
        # Convert input strings to integers
        num1_int = int(num1)
        num2_int = int(num2)
        
        # Calculate the sum
        sum_result = num1_int + num2_int
        
        # Convert the result back to string and return
        return str(sum_result)

    @staticmethod
    def subtract(num1, num2):
        # Convert input strings to integers
        num1_int = int(num1)
        num2_int = int(num2)
        
        # Calculate the difference
        diff_result = num1_int - num2_int
        
        # Convert the result back to string and return
        return str(diff_result)

    @staticmethod
    def multiply(num1, num2):
        # Convert input strings to integers
        num1_int = int(num1)
        num2_int = int(num2)
        
        # Calculate the product
        product_result = num1_int * num2_int
        
        # Convert the result back to string and return
        return str(product_result)