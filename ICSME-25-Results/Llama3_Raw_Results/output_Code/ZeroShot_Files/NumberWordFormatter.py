class NumberWordFormatter:
    def __init__(self):
        # Initialize a dictionary to store the word representation of numbers from 0 to 19
        self.ones = {
            0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
        }
        # Initialize a dictionary to store the word representation of tens
        self.tens = {
            0: '', 1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
            6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
        }
        # Initialize a dictionary to store the word representation of thousands, millions, and billions
        self.scales = {
            0: '', 1: 'thousand', 2: 'million', 3: 'billion'
        }

    def format(self, x):
        # Convert a number into words format
        return self.format_string(str(x))

    def format_string(self, x):
        # Convert a string representation of a number into words format
        # Split the number into integer and decimal parts
        parts = x.split('.')
        integer_part = parts[0]
        decimal_part = parts[1] if len(parts) > 1 else ''
        
        # Format the integer part
        integer_words = self.format_integer(integer_part)
        
        # Format the decimal part
        decimal_words = self.format_decimal(decimal_part)
        
        # Combine the integer and decimal parts
        if decimal_words:
            return f"{integer_words} point {decimal_words}"
        else:
            return integer_words

    def trans_two(self, s):
        # Convert a two-digit number into words format
        # If the number is less than 20, return its word representation directly
        if int(s) < 20:
            return self.ones[int(s)]
        # If the number is 20 or more, return the word representation of its tens and ones places
        else:
            return self.tens[int(s[0])] + ('' if int(s[1]) == 0 else ' ' + self.ones[int(s[1])])

    def trans_three(self, s):
        # Convert a three-digit number into words format
        # If the number is less than 100, return its word representation using trans_two
        if int(s) < 100:
            return self.trans_two(s)
        # If the number is 100 or more, return the word representation of its hundreds place and the rest
        else:
            return self.ones[int(s[0])] + ' hundred' + ('' if int(s[1:]) == 0 else ' and ' + self.trans_two(s[1:]))

    def parse_more(self, i):
        # Parse the thousand/million/billion suffix based on the index
        if i == 0:
            return ''
        else:
            return ' ' + self.scales[i]

    def format_integer(self, s):
        # Format the integer part of a number
        # Split the number into groups of three digits
        groups = []
        while s:
            groups.append(s[-3:])
            s = s[:-3]
        
        # Format each group and combine them
        words = ''
        for i in range(len(groups)):
            group = groups[-1 - i]
            # If the group is not empty, format it and add the corresponding suffix
            if group != '000':
                group_words = self.trans_three(group)
                words = group_words + self.parse_more(i) + ('' if words == '' else ' ') + words
        return words

    def format_decimal(self, s):
        # Format the decimal part of a number
        # Convert each digit to its word representation
        words = ' '.join(self.ones[int(d)] for d in s)
        return words