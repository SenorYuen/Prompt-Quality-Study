class BalancedBrackets:
    def __init__(self, expr):
        self.stack = []
        self.left_brackets = ["(", "{", "["]
        self.right_brackets = [")", "}", "]"]
        self.expr = expr

    def clear_expr(self):
        self.expr = ''.join([char for char in self.expr if char in self.left_brackets or char in self.right_brackets])

    def check_balanced_brackets(self):
        for char in self.expr:
            if char in self.left_brackets:
                self.stack.append(char)
            elif char in self.right_brackets:
                if not self.stack:
                    return False
                top = self.stack.pop()
                if self.left_brackets.index(top) != self.right_brackets.index(char):
                    return False
        return not self.stack