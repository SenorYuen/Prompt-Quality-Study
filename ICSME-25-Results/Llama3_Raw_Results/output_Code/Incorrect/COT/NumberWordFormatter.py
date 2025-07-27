class NumberWordFormatter:
    def __init__(self):
        # Initialize a NumberWordFormatter object
        # Define lists for numbers, teens, tens, and suffixes
        self.NUMBER = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.NUMBER_TEEN = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN",
                            "EIGHTEEN", "NINETEEN"]
        self.NUMBER_TEN = ["TEN", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.NUMBER_MORE = ["", "THOUSAND", "MILLION", "BILLION"]
        self.NUMBER_SUFFIX = ["k", "w", "", "m", "", "", "b", "", "", "t", "", "", "p", "", "", "e"]

    def format(self, x):
        # Convert a number into words format
        # Get "x" as int or float which is the number to be converted into words format
        # Return the number in words format as str
        if isinstance(x, int):
            return self.format_integer(x) + " ONLY"
        elif isinstance(x, float):
            integer_part = int(x)
            decimal_part = int((x - integer_part) * 100)
            return self.format_integer(integer_part) + " POINT " + self.format_integer(decimal_part) + " ONLY"

    def format_string(self, x):
        # Convert a string representation of a number into words format
        # Get "x" as str which is the string representation of a number
        # Return the number in words format as str
        return self.format(int(x))

    def trans_two(self, s):
        # Convert a two-digit number into words format
        # Get "s" as str which is the two-digit number
        # Return the number in words format as str
        num = int(s)
        if num < 10:
            return self.NUMBER[num]
        elif num < 20:
            return self.NUMBER_TEEN[num - 10]
        else:
            tens, ones = divmod(num, 10)
            return self.NUMBER_TEN[tens - 1] + (" " + self.NUMBER[ones] if ones != 0 else "")

    def trans_three(self, s):
        # Convert a three-digit number into words format
        # Get "s" as str which is the three-digit number
        # Return the number in words format as str
        num = int(s)
        if num < 10:
            return self.NUMBER[num]
        elif num < 20:
            return self.NUMBER_TEEN[num - 10]
        elif num < 100:
            return self.trans_two(s)
        else:
            hundreds, rest = divmod(num, 100)
            return self.NUMBER[hundreds] + " HUNDRED" + (" AND " + self.trans_two(str(rest)) if rest != 0 else "")

    def parse_more(self, i):
        # Parse the thousand/million/billion suffix based on the index
        # Get "i" as int which is the index representing the magnitude (thousand, million, billion)
        # Return the corresponding suffix for the magnitude as str
        return self.NUMBER_MORE[i]

    def format_integer(self, x):
        # Helper function to format integer part
        if x == 0:
            return "ZERO"
        result = ""
        i = 0
        while x > 0:
            if x % 1000 != 0:
                result = self.trans_three(str(x % 1000)) + " " + self.parse_more(i) + (" " + result if result != "" else "")
            x //= 1000
            i += 1
        return result.strip()