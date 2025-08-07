class NumberWordFormatter:
    def __init__(self):
        """
        Initialize NumberWordFormatter object.
        """
        # Define basic number words for quick lookup
        self.units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        self.teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def format(self, x):
        """
        Converts a number into words format
        :return: str, the number in words format
        """
        if isinstance(x, str):
            return self.format_string(x)
        elif isinstance(x, (int, float)):
            return self.format_string(str(x))
        else:
            raise ValueError("Unsupported type")

    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :return: str, the number in words format
        """
        if '.' in x:
            integer_part, decimal_part = x.split('.')
            integer_words = self.convert_integer_to_words(integer_part)
            decimal_words = self.convert_integer_to_words(decimal_part)
            return f"{integer_words} point {decimal_words}"
        else:
            return self.convert_integer_to_words(x)

    def convert_integer_to_words(self, num_str):
        """
        Converts an integer string into words format
        :return: str, the number in words format
        """
        num = int(num_str)
        if num == 0:
            return "Zero"
        
        words = ""
        place = 0

        while num > 0:
            if num % 1000 != 0:
                words = self.trans_three(num % 1000) + (self.thousands[place] and " " + self.thousands[place] or "") + " " + words
            num //= 1000
            place += 1

        return words.strip()

    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :return: str, the number in words format
        """
        num = int(s)
        if num < 10:
            return self.units[num]
        elif num < 20:
            return self.teens[num - 10]
        else:
            return self.tens[num // 10] + (num % 10 != 0 and " " + self.units[num % 10] or "")

    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :return: str, the number in words format
        """
        num = int(s)
        if num < 100:
            return self.trans_two(s)
        else:
            return self.units[num // 100] + " Hundred" + (num % 100 != 0 and " " + self.trans_two(num % 100) or "")

    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :return: str, the corresponding suffix for the magnitude
        """
        return self.thousands[i] if i < len(self.thousands) else ""

# Example usage:
# formatter = NumberWordFormatter()
# print(formatter.format(1234567.89))  # Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven point Eighty Nine"