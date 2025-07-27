class BalancedBrackets:
    def __init__(self, expr):
        # Initialize the class with an expression
        # Accept "expr" as str which is the expression to check for balanced bracket
        self.stack = []
        self.left_brackets = ["(", "{", "["]
        self.right_brackets = [")", "}", "]"]
        self.expr = expr

    def clear_expr(self):
        # Clear the expression of all characters that are not brackets
        self.expr = ''.join([char for char in self.expr if char in self.left_brackets or char in self.right_brackets])

    def check_balanced_brackets(self):
        # Check if the expression has balanced brackets
        # Return True if the expression has balanced brackets, False otherwise
        self.clear_expr()
        for char in self.expr:
            if char in self.left_brackets:
                # If the character is a left bracket, push it to the stack
                self.stack.append(char)
            elif char in self.right_brackets:
                # If the character is a right bracket, check if the stack is empty or the top of the stack does not match
                if not self.stack:
                    return False
                top = self.stack.pop()
                if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
                    return False
        # If the stack is empty after iterating through the expression, the brackets are balanced
        return not self.stack