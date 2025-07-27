class NumberWordFormatter:
    """
    This is a class that provides to convert numbers into their corresponding English word representation, 
    including handling the conversion of both the integer and decimal parts, and incorporating appropriate connectors and units.
    """

    def __init__(self):
        """
        Initialize NumberWordFormatter object.
        """
        self.NUMBER = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.NUMBER_TEEN = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN",
                            "EIGHTEEN",
                            "NINETEEN"]
        self.NUMBER_TEN = ["TEN", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.NUMBER_MORE = ["", "THOUSAND", "MILLION", "BILLION"]
        self.NUMBER_SUFFIX = ["k", "w", "", "m", "", "", "b", "", "", "t", "", "", "p", "", "", "e"]

    def format(self, x):
        # Convert the number into a string to handle both integer and decimal parts
        x_str = str(x)
        
        # Check if the number has a decimal part
        if '.' in x_str:
            # Split the number into integer and decimal parts
            integer_part, decimal_part = x_str.split('.')
            
            # Convert the integer part into words
            integer_words = self.format_string(integer_part)
            
            # Convert the decimal part into words
            decimal_words = self.format_string(decimal_part)
            
            # Combine the integer and decimal parts into a single string
            return f"{integer_words} POINT {decimal_words}"
        else:
            # Convert the integer part into words
            return self.format_string(x_str)

    def format_string(self, x):
        # Convert the string representation of the number into an integer
        x_int = int(x)
        
        # Check if the number is less than 10
        if x_int < 10:
            # Return the word representation of the number
            return self.NUMBER[x_int]
        # Check if the number is between 10 and 19
        elif x_int < 20:
            # Return the word representation of the number
            return self.NUMBER_TEEN[x_int - 10]
        # Check if the number is between 20 and 99
        elif x_int < 100:
            # Get the tens digit
            tens_digit = x_int // 10
            
            # Get the ones digit
            ones_digit = x_int % 10
            
            # Return the word representation of the number
            if ones_digit == 0:
                return self.NUMBER_TEN[tens_digit - 1]
            else:
                return f"{self.NUMBER_TEN[tens_digit - 1]} {self.NUMBER[ones_digit]}"
        # Check if the number is between 100 and 999
        elif x_int < 1000:
            # Get the hundreds digit
            hundreds_digit = x_int // 100
            
            # Get the remaining digits
            remaining_digits = x_int % 100
            
            # Return the word representation of the number
            if remaining_digits == 0:
                return f"{self.NUMBER[hundreds_digit]} HUNDRED"
            else:
                return f"{self.NUMBER[hundreds_digit]} HUNDRED AND {self.trans_two(str(remaining_digits))}"
        # Check if the number is 1000 or more
        else:
            # Initialize the result string
            result = ""
            
            # Initialize the index
            i = 0
            
            # Loop through the number from right to left
            while x_int > 0:
                # Get the current three digits
                current_three_digits = x_int % 1000
                
                # If the current three digits are not zero, add them to the result string
                if current_three_digits != 0:
                    # Add the word representation of the current three digits to the result string
                    result = f"{self.trans_three(str(current_three_digits))} {self.parse_more(i)} {result}"
                
                # Move to the next three digits
                x_int //= 1000
                
                # Increment the index
                i += 1
            
            # Remove any trailing spaces from the result string
            result = result.strip()
            
            # Add " ONLY" to the end of the result string
            result += " ONLY"
            
            # Return the result string
            return result

    def trans_two(self, s):
        # Convert the two-digit number into an integer
        s_int = int(s)
        
        # Check if the number is less than 10
        if s_int < 10:
            # Return the word representation of the number
            return self.NUMBER[s_int]
        # Check if the number is between 10 and 19
        elif s_int < 20:
            # Return the word representation of the number
            return self.NUMBER_TEEN[s_int - 10]
        # Check if the number is between 20 and 99
        else:
            # Get the tens digit
            tens_digit = s_int // 10
            
            # Get the ones digit
            ones_digit = s_int % 10
            
            # Return the word representation of the number
            if ones_digit == 0:
                return self.NUMBER_TEN[tens_digit - 1]
            else:
                return f"{self.NUMBER_TEN[tens_digit - 1]} {self.NUMBER[ones_digit]}"

    def trans_three(self, s):
        # Convert the three-digit number into an integer
        s_int = int(s)
        
        # Check if the number is less than 10
        if s_int < 10:
            # Return the word representation of the number
            return self.NUMBER[s_int]
        # Check if the number is between 10 and 19
        elif s_int < 20:
            # Return the word representation of the number
            return self.NUMBER_TEEN[s_int - 10]
        # Check if the number is between 20 and 99
        elif s_int < 100:
            # Get the tens digit
            tens_digit = s_int // 10
            
            # Get the ones digit
            ones_digit = s_int % 10
            
            # Return the word representation of the number
            if ones_digit == 0:
                return self.NUMBER_TEN[tens_digit - 1]
            else:
                return f"{self.NUMBER_TEN[tens_digit - 1]} {self.NUMBER[ones_digit]}"
        # Check if the number is between 100 and 999
        else:
            # Get the hundreds digit
            hundreds_digit = s_int // 100
            
            # Get the remaining digits
            remaining_digits = s_int % 100
            
            # Return the word representation of the number
            if remaining_digits == 0:
                return f"{self.NUMBER[hundreds_digit]} HUNDRED"
            else:
                return f"{self.NUMBER[hundreds_digit]} HUNDRED AND {self.trans_two(str(remaining_digits))}"

    def parse_more(self, i):
        # Return the word representation of the magnitude
        return self.NUMBER_MORE[i]