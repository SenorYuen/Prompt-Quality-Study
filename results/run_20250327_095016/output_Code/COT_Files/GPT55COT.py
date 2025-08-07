class Manacher:
    def __init__(self, input_string: str):
        self.input_string = input_string

    def palindromic_length(self, center: int, diff: int, string: str) -> int:
        while center - diff >= 0 and center + diff < len(string) and string[center - diff] == string[center + diff]:
            diff += 1
        return diff - 1

    def palindromic_string(self) -> str:
        if not self.input_string:
            return ""

        # Transform the original string to a new format with separators
        string = '|'.join(f'#{self.input_string}#')
        p = [0] * len(string)
        center = right = 0

        for i in range(1, len(string) - 1):
            mirror = 2 * center - i

            if i < right:
                p[i] = min(right - i, p[mirror])

            p[i] += self.palindromic_length(i, p[i] + 1, string)

            if i + p[i] > right:
                center, right = i, i + p[i]

        max_len, center_index = max((n, i) for i, n in enumerate(p))
        start = (center_index - max_len) // 2
        return self.input_string[start:start + max_len]