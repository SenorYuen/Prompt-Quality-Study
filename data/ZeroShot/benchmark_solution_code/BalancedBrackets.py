'''
# This is a class that checks for bracket matching

class BalancedBrackets:
    def __init__(self, expr):
        """
        Initializes the class with an expression.
        """

    def clear_expr(self):
        """
        Clears the expression of all characters that are not brackets.
        """

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        """
'''

class BalancedBrackets:
    def __init__(self, expr):
        self.stack = []
        self.left_brackets = ["(", "{", "["]
        self.right_brackets = [")", "}", "]"]
        self.expr = expr

    def clear_expr(self):
        self.expr = ''.join(c for c in self.expr if (c in self.left_brackets or c in self.right_brackets))

    def check_balanced_brackets(self):
        self.clear_expr()
        for Brkt in self.expr:
            if Brkt in self.left_brackets:
                self.stack.append(Brkt)
            else:
                Current_Brkt = self.stack.pop()
                if Current_Brkt == "(":
                    if Brkt != ")":
                        return False
                if Current_Brkt == "{":
                    if Brkt != "}":
                        return False
                if Current_Brkt == "[":
                    if Brkt != "]":
                        return False
        if self.stack:
            return False
        return True