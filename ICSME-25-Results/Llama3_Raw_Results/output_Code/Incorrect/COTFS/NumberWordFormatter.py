class NumberWordFormatter:
    def __init__(self):
        self.NUMBER = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.NUMBER_TEEN = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN",
                            "EIGHTEEN", "NINETEEN"]
        self.NUMBER_TEN = ["", "TEN", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.NUMBER_MORE = ["", "THOUSAND", "MILLION", "BILLION"]
        self.NUMBER_SUFFIX = ["k", "w", "", "m", "", "", "b", "", "", "t", "", "", "p", "", "", "e"]

    def format(self, x):
        if isinstance(x, int):
            return self.format_int(x) + " ONLY"
        elif isinstance(x, float):
            integer_part = int(x)
            decimal_part = str(x).split('.')[1]
            return self.format_int(integer_part) + " POINT " + self.format_decimal(decimal_part) + " ONLY"

    def format_string(self, x):
        if '.' in x:
            integer_part, decimal_part = x.split('.')
            return self.format_int(int(integer_part)) + " POINT " + self.format_decimal(decimal_part) + " ONLY"
        else:
            return self.format_int(int(x)) + " ONLY"

    def trans_two(self, s):
        if int(s) < 10:
            return self.NUMBER[int(s)]
        elif int(s) < 20:
            return self.NUMBER_TEEN[int(s) - 10]
        else:
            tens, ones = s
            if ones == '0':
                return self.NUMBER_TEN[int(tens)]
            else:
                return self.NUMBER_TEN[int(tens)] + " " + self.NUMBER[int(ones)]

    def trans_three(self, s):
        hundreds, tens, ones = s
        if hundreds == '0':
            return self.trans_two(tens + ones)
        elif tens == '0' and ones == '0':
            return self.NUMBER[int(hundreds)] + " HUNDRED"
        else:
            return self.NUMBER[int(hundreds)] + " HUNDRED AND " + self.trans_two(tens + ones)

    def parse_more(self, i):
        return self.NUMBER_MORE[i]

    def format_int(self, x):
        if x == 0:
            return "ZERO"
        result = ""
        i = 0
        while x > 0:
            if x % 1000 != 0:
                result = self.trans_three(str(x % 1000).zfill(3)) + " " + self.parse_more(i) + " " + result
            x //= 1000
            i += 1
        return result.strip()

    def format_decimal(self, x):
        result = ""
        for digit in x:
            result += self.NUMBER[int(digit)] + " "
        return result.strip()