class NumberWordFormatter:
    def __init__(self):
        self.NUMBER = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.NUMBER_TEEN = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN",
                            "EIGHTEEN", "NINETEEN"]
        self.NUMBER_TEN = ["TEN", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.NUMBER_MORE = ["", "THOUSAND", "MILLION", "BILLION"]
        self.NUMBER_SUFFIX = ["k", "w", "", "m", "", "", "b", "", "", "t", "", "", "p", "", "", "e"]

    def format(self, x):
        if isinstance(x, float):
            integer_part, decimal_part = str(x).split(".")
            integer_part = self.format_string(integer_part)
            decimal_part = self.format_string(decimal_part)
            return f"{integer_part} POINT {decimal_part} ONLY"
        else:
            return f"{self.format_string(str(x))} ONLY"

    def format_string(self, x):
        if x == "0":
            return "ZERO"
        parts = []
        length = len(x)
        num_groups = (length + 2) // 3
        x = x.zfill(num_groups * 3)
        for i in range(num_groups):
            start = i * 3
            end = start + 3
            group = x[start:end]
            if group != "000":
                part = self.trans_three(group)
                if i < len(self.NUMBER_MORE):
                    part += f" {self.NUMBER_MORE[num_groups - i - 1]}"
                parts.append(part.strip())
        return " ".join(parts)

    def trans_two(self, s):
        if s[0] == '0':
            return self.NUMBER[int(s[1])]
        elif s[0] == '1':
            return self.NUMBER_TEEN[int(s[1])]
        else:
            return f"{self.NUMBER_TEN[int(s[0]) - 1]} {self.NUMBER[int(s[1])]}".strip()

    def trans_three(self, s):
        if s[0] == '0':
            return self.trans_two(s[1:])
        else:
            return f"{self.NUMBER[int(s[0])]} HUNDRED AND {self.trans_two(s[1:])}".strip()

    def parse_more(self, i):
        if i < len(self.NUMBER_MORE):
            return self.NUMBER_MORE[i]
        return ""