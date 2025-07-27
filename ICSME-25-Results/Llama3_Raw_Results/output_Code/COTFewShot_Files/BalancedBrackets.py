class BalancedBrackets:
    def __init__(self, expr):
        # Initialize the class with an expression
        self.stack = []
        self.left_brackets = ["(", "{", "["]
        self.right_brackets = [")", "}", "]"]
        self.expr = expr

    def clear_expr(self):
        # Clear the expression of all characters that are not brackets
        self.expr = ''.join([char for char in self.expr if char in self.left_brackets or char in self.right_brackets])
        return self.expr

    def check_balanced_brackets(self):
        # Check if the expression has balanced brackets
        self.clear_expr()
        for char in self.expr:
            if char in self.left_brackets:
                self.stack.append(char)
            elif char in self.right_brackets:
                if not self.stack:
                    return False
                left_bracket = self.stack.pop()
                if (char == ')' and left_bracket != '(') or (char == '}' and left_bracket != '{') or (char == ']' and left_bracket != '['):
                    return False
        return not self.stack