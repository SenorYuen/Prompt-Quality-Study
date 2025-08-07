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
            integer_part = int(x)
            decimal_part = round((x - integer_part) * 100)
            words = self.format_string(str(integer_part))
            if decimal_part > 0:
                words += " POINT " + " ".join(self.NUMBER[int(d)] for d in str(decimal_part))
            return words + " ONLY"
        elif isinstance(x, int):
            return self.format_string(str(x)) + " ONLY"
        else:
            raise ValueError("Input must be an integer or float")

    def format_string(self, x):
        length = len(x)
        if length == 0:
            return ""
        elif length <= 3:
            return self.trans_three(x)
        else:
            num_chunks = (length + 2) // 3
            words = []
            for i in range(num_chunks):
                start = max(0, length - 3 * (i + 1))
                end = length - 3 * i
                chunk_words = self.trans_three(x[start:end])
                if chunk_words:
                    words.append(chunk_words + " " + self.parse_more(i))
            return " ".join(reversed(words)).strip()

    def trans_two(self, s):
        if len(s) == 1:
            return self.NUMBER[int(s)]
        elif s[0] == '1':
            return self.NUMBER_TEEN[int(s[1])]
        else:
            ten = self.NUMBER_TEN[int(s[0]) - 1]
            one = self.NUMBER[int(s[1])]
            return ten + (" " + one if one else "")

    def trans_three(self, s):
        if len(s) == 3 and s[0] != '0':
            return self.NUMBER[int(s[0])] + " HUNDRED" + (" AND " + self.trans_two(s[1:]) if s[1:] != "00" else "")
        else:
            return self.trans_two(s)

    def parse_more(self, i):
        return self.NUMBER_MORE[i] if i < len(self.NUMBER_MORE) else ""