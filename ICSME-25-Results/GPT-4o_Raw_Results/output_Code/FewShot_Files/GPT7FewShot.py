class BalancedBrackets:
    """
    This is a class that checks for bracket matching
    """

    def __init__(self, expr):
        """
        Initializes the class with an expression.
        :param expr: The expression to check for balanced brackets, str.
        """
        self.stack = []
        self.left_brackets = ["(", "{", "["]
        self.right_brackets = [")", "}", "]"]
        self.expr = expr

    def clear_expr(self):
        """
        Clears the expression of all characters that are not brackets.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.clear_expr()
        >>> b.expr
        '()'
        """
        # Use a list comprehension to filter only bracket characters
        self.expr = ''.join([char for char in self.expr if char in self.left_brackets + self.right_brackets])

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets()
        True
        """
        # Clear the expression to contain only brackets
        self.clear_expr()

        # Dictionary to map left brackets to their corresponding right brackets
        bracket_map = {")": "(", "}": "{", "]": "["}

        # Iterate through each character in the expression
        for char in self.expr:
            # If it's a left bracket, push it onto the stack
            if char in self.left_brackets:
                self.stack.append(char)
            # If it's a right bracket
            elif char in self.right_brackets:
                # If the stack is empty or the top of the stack doesn't match the corresponding left bracket, return False
                if not self.stack or self.stack.pop() != bracket_map[char]:
                    return False

        # If the stack is empty, all brackets were matched; otherwise, return False
        return not self.stack