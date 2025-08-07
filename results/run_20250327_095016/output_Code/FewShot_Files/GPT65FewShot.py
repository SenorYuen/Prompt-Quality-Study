class NumberWordFormatter:
    def __init__(self):
        self.NUMBER = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.NUMBER_TEEN = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
        self.NUMBER_TEN = ["", "TEN", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.NUMBER_MORE = ["", "THOUSAND", "MILLION", "BILLION"]
        self.NUMBER_SUFFIX = ["k", "w", "", "m", "", "", "b", "", "", "t", "", "", "p", "", "", "e"]

    def format(self, x):
        if isinstance(x, float):
            integer_part = int(x)
            decimal_part = int(round((x - integer_part) * 100))
            return f"{self.format_string(str(integer_part))} POINT {self.trans_two(str(decimal_part))} ONLY"
        else:
            return f"{self.format_string(str(x))} ONLY"

    def format_string(self, x):
        if x == "0":
            return "ZERO"
        
        x = x.zfill((len(x) + 2) // 3 * 3)  # Pad with zeros to make it a multiple of 3
        parts = [x[i:i+3] for i in range(0, len(x), 3)]
        
        words = []
        for i, part in enumerate(parts):
            if part != "000":
                words.append(self.trans_three(part))
                if i < len(parts) - 1:
                    words.append(self.NUMBER_MORE[len(parts) - i - 1])
        
        return " ".join(word for word in words if word)

    def trans_two(self, s):
        if len(s) == 1:
            return self.NUMBER[int(s)]
        elif s[0] == '1':
            return self.NUMBER_TEEN[int(s[1])]
        else:
            return f"{self.NUMBER_TEN[int(s[0])]} {self.NUMBER[int(s[1])]}".strip()

    def trans_three(self, s):
        if s[0] == '0':
            return self.trans_two(s[1:])
        else:
            return f"{self.NUMBER[int(s[0])]} HUNDRED {'AND ' + self.trans_two(s[1:]) if s[1:] != '00' else ''}".strip()

    def parse_more(self, i):
        return self.NUMBER_MORE[i]