class Manacher:
    def __init__(self, input_string):
        self.input_string = input_string

    def palindromic_length(self, center, diff, string):
        while center - diff >= 0 and center + diff < len(string) and string[center - diff] == string[center + diff]:
            diff += 1
        return diff - 1

    def palindromic_string(self):
        if not self.input_string:
            return ""

        # Transform the input string to avoid even/odd length issues
        string = '|' + '|'.join(self.input_string) + '|'
        n = len(string)
        P = [0] * n
        C = R = 0  # Center and right boundary of the current palindrome

        for i in range(n):
            mirror = 2 * C - i
            if i < R:
                P[i] = min(R - i, P[mirror])

            P[i] = self.palindromic_length(i, P[i] + 1, string)

            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P
        max_len, center_index = max((n, i) for i, n in enumerate(P))
        start = (center_index - max_len) // 2
        return self.input_string[start:start + max_len]