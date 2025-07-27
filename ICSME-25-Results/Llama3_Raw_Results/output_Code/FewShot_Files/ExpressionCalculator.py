from collections import deque
from decimal import Decimal

class ExpressionCalculator:
    """
    This is a class in Python that can perform calculations with basic arithmetic operations, including addition, subtraction, multiplication, division, and modulo.
    """

    def __init__(self):
        """
        Initialize the expression calculator
        """
        # Initialize an empty stack to store operands
        self.postfix_stack = deque()
        # Define operator precedence
        self.operat_priority = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}

    def calculate(self, expression):
        """
        Calculate the result of the given postfix expression
        :param expression: string, the postfix expression to be calculated
        :return: float, the calculated result
        """
        # Split the expression into tokens (operators and operands)
        tokens = expression.split()
        # Initialize an empty stack to store operands
        stack = deque()
        # Iterate over each token in the expression
        for token in tokens:
            # If the token is an operand, push it to the stack
            if token not in self.operat_priority:
                stack.append(Decimal(token))
            # If the token is an operator, pop two operands from the stack, perform the operation, and push the result back to the stack
            else:
                second_value = stack.pop()
                first_value = stack.pop()
                result = self._calculate(first_value, second_value, token)
                stack.append(result)
        # The final result is the only element left in the stack
        return stack[0]

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        """
        # Remove any whitespace from the expression
        expression = self.transform(expression)
        # Initialize an empty stack to store operators
        operator_stack = deque()
        # Initialize an empty list to store the postfix expression
        postfix_expression = []
        # Iterate over each character in the expression
        for char in expression:
            # If the character is an operand, add it to the postfix expression
            if char.isdigit():
                postfix_expression.append(char)
            # If the character is an operator, pop operators from the stack and add them to the postfix expression until an operator with lower precedence is found, then push the current operator to the stack
            elif char in self.operat_priority:
                while operator_stack and self.compare(operator_stack[-1], char):
                    postfix_expression.append(operator_stack.pop())
                operator_stack.append(char)
            # If the character is a left parenthesis, push it to the stack
            elif char == '(':
                operator_stack.append(char)
            # If the character is a right parenthesis, pop operators from the stack and add them to the postfix expression until a left parenthesis is found, then discard the left parenthesis
            elif char == ')':
                while operator_stack[-1] != '(':
                    postfix_expression.append(operator_stack.pop())
                operator_stack.pop()
        # Pop any remaining operators from the stack and add them to the postfix expression
        while operator_stack:
            postfix_expression.append(operator_stack.pop())
        # Join the postfix expression into a string and store it in the postfix_stack attribute
        self.postfix_stack = ' '.join(postfix_expression)

    @staticmethod
    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        """
        # Define the set of operators
        operators = {'+', '-', '*', '/', '(', ')', '%'}
        # Check if the character is in the set of operators
        return c in operators

    def compare(self, cur, peek):
        """
        Compare the precedence of two operators
        :param cur: string, the current operator
        :param peek: string, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        """
        # Compare the precedence of the two operators
        return self.operat_priority[cur] >= self.operat_priority[peek]

    @staticmethod
    def _calculate(first_value, second_value, current_op):
        """
        Perform the mathematical calculation based on the given operands and operator
        :param first_value: string, the first operand
        :param second_value: string, the second operand
        :param current_op: string, the operator
        :return: decimal.Decimal, the calculated result
        """
        # Perform the calculation based on the operator
        if current_op == '+':
            return first_value + second_value
        elif current_op == '-':
            return first_value - second_value
        elif current_op == '*':
            return first_value * second_value
        elif current_op == '/':
            return first_value / second_value
        elif current_op == '%':
            return first_value % second_value

    @staticmethod
    def transform(expression):
        """
        Transform the infix expression to a format suitable for conversion
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        """
        # Remove any whitespace from the expression
        return expression.replace(' ', '')