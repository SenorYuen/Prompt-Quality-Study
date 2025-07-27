class BalancedBrackets:
    def __init__(self, expr):
        """
        Initializes the class with an expression.
        :param expr: The input expression string to be checked for balanced brackets.
        """
        self.expr = expr

    def clear_expr(self):
        """
        Clears the expression of all characters that are not brackets.
        Retains only '()', '{}', and '[]' characters in the expression.
        """
        brackets = set("(){}[]")
        self.expr = ''.join([char for char in self.expr if char in brackets])

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        """
        stack = []
        # Dictionary to hold matching pairs of brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in self.expr:
            if char in bracket_map.values():
                # If the character is an opening bracket, push it onto the stack
                stack.append(char)
            elif char in bracket_map:
                # If the character is a closing bracket, check for balance
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()  # Pop the matching opening bracket
                else:
                    return False  # Unbalanced due to mismatch or empty stack

        # If stack is empty, all brackets were matched; otherwise, unbalanced
        return not stack