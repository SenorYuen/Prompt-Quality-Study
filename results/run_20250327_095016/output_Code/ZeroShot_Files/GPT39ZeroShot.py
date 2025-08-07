from collections import deque
from decimal import Decimal

class ExpressionCalculator:
    def __init__(self):
        """
        Initialize the expression calculator
        """
        self.postfix_stack = deque()
        self.operat_priority = [0, 3, 2, 1, -1, 1, 0, 2]

    def calculate(self, expression):
        """
        Calculate the result of the given postfix expression
        :param expression: string, the postfix expression
        :return: float, the calculated result
        """
        stack = deque()
        for token in expression.split():
            if token.isdigit() or '.' in token:  # Check if token is a number
                stack.append(Decimal(token))
            else:
                second_value = stack.pop()
                first_value = stack.pop()
                result = self._calculate(first_value, second_value, token)
                stack.append(result)
        return float(stack.pop())

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression
        :return: string, the postfix expression
        """
        output = []
        operators = deque()
        for token in self.transform(expression):
            if token.isdigit() or '.' in token:
                output.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()  # Remove '(' from stack
            else:
                while operators and self.compare(token, operators[-1]):
                    output.append(operators.pop())
                operators.append(token)
        
        while operators:
            output.append(operators.pop())
        
        return ' '.join(output)

    @staticmethod
    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        :param c: char, the character to check
        :return: bool, True if the character is an operator, False otherwise
        """
        return c in {'+', '-', '*', '/', '(', ')', '%'}

    def compare(self, cur, peek):
        """
        Compare the precedence of two operators
        :param cur: char, the current operator
        :param peek: char, the operator to compare with
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        """
        return self.operat_priority[self._get_priority(cur)] <= self.operat_priority[self._get_priority(peek)]

    @staticmethod
    def _calculate(first_value, second_value, current_op):
        """
        Perform the mathematical calculation based on the given operands and operator
        :param first_value: decimal.Decimal, the first operand
        :param second_value: decimal.Decimal, the second operand
        :param current_op: char, the operator
        :return: decimal.Decimal, the calculated result
        """
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
        else:
            raise ValueError(f"Unknown operator: {current_op}")

    @staticmethod
    def transform(expression):
        """
        Transform the infix expression to a format suitable for conversion
        :param expression: string, the infix expression
        :return: list, the transformed expression as a list of tokens
        """
        tokens = []
        current_num = []
        for char in expression:
            if char.isdigit() or char == '.':
                current_num.append(char)
            else:
                if current_num:
                    tokens.append(''.join(current_num))
                    current_num = []
                if char.strip():  # Ignore spaces
                    tokens.append(char)
        if current_num:
            tokens.append(''.join(current_num))
        return tokens

    def _get_priority(self, op):
        """
        Get the priority index for an operator
        :param op: char, the operator
        :return: int, the index in the priority list
        """
        return {'+': 1, '-': 2, '*': 3, '/': 4, '%': 5, '(': 6, ')': 7}.get(op, 0)