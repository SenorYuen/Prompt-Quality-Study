# This is a class that checks for bracket matching

class BalancedBrackets:
    def __init__(self, expr):
        # Initializes the class with an expression.
        self.expr = expr

    def clear_expr(self):
        # Clears the expression of all characters that are not brackets.
        self.expr = ''.join([char for char in self.expr if char in '()[]{}'])

    def check_balanced_brackets(self):
        # Checks if the expression has balanced brackets.
        # :return: True if the expression has balanced brackets, False otherwise.
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Iterate over each character in the expression
        for char in self.expr:
            # If the character is an opening bracket, push it onto the stack
            if char in bracket_map.values():
                stack.append(char)
            # If the character is a closing bracket, check if the stack is empty or the top of the stack does not match
            elif char in bracket_map.keys():
                if not stack or stack.pop() != bracket_map[char]:
                    return False
        
        # If the stack is empty after iterating over the entire expression, the brackets are balanced
        return not stack


# Example usage:
if __name__ == "__main__":
    # Create an instance of the BalancedBrackets class
    bb = BalancedBrackets("({[]})")
    
    # Clear the expression of non-bracket characters
    bb.clear_expr()
    
    # Check if the expression has balanced brackets
    print(bb.check_balanced_brackets())  # Output: True

    # Create an instance of the BalancedBrackets class with unbalanced brackets
    bb_unbalanced = BalancedBrackets("({[})")
    
    # Clear the expression of non-bracket characters
    bb_unbalanced.clear_expr()
    
    # Check if the expression has balanced brackets
    print(bb_unbalanced.check_balanced_brackets())  # Output: False