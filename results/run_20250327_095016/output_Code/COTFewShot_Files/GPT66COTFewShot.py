class NumericEntityUnescaper:
    def __init__(self):
        pass

    def replace(self, string):
        result = []
        i = 0
        while i < len(string):
            if string[i] == '&' and i + 1 < len(string) and string[i + 1] == '#':
                i += 2
                is_hex = False
                if i < len(string) and (string[i] == 'x' or string[i] == 'X'):
                    is_hex = True
                    i += 1

                num_str = []
                while i < len(string) and (string[i].isdigit() or (is_hex and self.is_hex_char(string[i]))):
                    num_str.append(string[i])
                    i += 1

                if i < len(string) and string[i] == ';':
                    i += 1
                    try:
                        if is_hex:
                            char = chr(int(''.join(num_str), 16))
                        else:
                            char = chr(int(''.join(num_str), 10))
                        result.append(char)
                    except (ValueError, OverflowError):
                        result.append('&#' + ''.join(num_str) + ';')
                else:
                    result.append('&#' + ''.join(num_str))
            else:
                result.append(string[i])
                i += 1

        return ''.join(result)

    @staticmethod
    def is_hex_char(char):
        return char.isdigit() or ('a' <= char.lower() <= 'f')