class BalancedBrackets:
    """
    This is a class that checks for bracket matching
    """

    def __init__(self, expr):
        """
        Initializes the class with an expression.
        :param expr: The expression to check for balanced brackets,str.
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
        # Use a list comprehension to filter out non-bracket characters
        self.expr = ''.join([char for char in self.expr if char in self.left_brackets + self.right_brackets])

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets()
        True
        """
        # Create a dictionary to map closing brackets to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Iterate over each character in the expression
        for char in self.expr:
            # If the character is an opening bracket, push it onto the stack
            if char in self.left_brackets:
                self.stack.append(char)
            # If the character is a closing bracket, check if the stack is empty or the top of the stack does not match
            elif char in self.right_brackets:
                if not self.stack or self.stack.pop() != bracket_map[char]:
                    return False
        
        # If the stack is empty after iterating over the entire expression, the brackets are balanced
        return not self.stack