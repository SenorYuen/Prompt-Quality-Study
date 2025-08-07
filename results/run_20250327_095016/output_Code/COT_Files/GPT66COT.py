class NumericEntityUnescaper:
    
    def __init__(self):
        pass

    def replace(self, string):
        result = []
        i = 0
        length = len(string)
        while i < length:
            if string[i] == '&' and i + 1 < length and string[i + 1] == '#':
                is_hex = False
                start = i + 2
                if start < length and (string[start] == 'x' or string[start] == 'X'):
                    is_hex = True
                    start += 1
                end = start
                while end < length and (string[end].isdigit() or (is_hex and self.is_hex_char(string[end]))):
                    end += 1
                if end < length and string[end] == ';':
                    entity = string[start:end]
                    try:
                        if is_hex:
                            codepoint = int(entity, 16)
                        else:
                            codepoint = int(entity)
                        result.append(chr(codepoint))
                        i = end + 1
                        continue
                    except ValueError:
                        pass
            result.append(string[i])
            i += 1
        return ''.join(result)

    @staticmethod
    def is_hex_char(char):
        return char.isdigit() or ('a' <= char <= 'f') or ('A' <= char <= 'F')