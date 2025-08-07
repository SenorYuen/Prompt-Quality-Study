from collections import deque
from decimal import Decimal

class ExpressionCalculator:
    def __init__(self):
        self.postfix_stack = deque()
        self.operator_priority = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '(': 0, ')': 0}

    def calculate(self, expression):
        # Prepare expression and convert it to postfix
        self.prepare(expression)
        stack = []
        for token in self.postfix_stack:
            if token.isdigit():
                stack.append(Decimal(token))
            else:
                b = stack.pop()
                a = stack.pop()
                result = self._calculate(a, b, token)
                stack.append(result)
        return float(stack.pop())

    def prepare(self, expression):
        # Transform expression and convert to postfix notation
        transformed_expr = self.transform(expression)
        op_stack = deque()
        for char in transformed_expr:
            if char.isdigit():
                self.postfix_stack.append(char)
            elif char == '(':
                op_stack.append(char)
            elif char == ')':
                top_op = op_stack.pop()
                while top_op != '(':
                    self.postfix_stack.append(top_op)
                    top_op = op_stack.pop()
            else:
                while op_stack and self.compare(char, op_stack[-1]):
                    self.postfix_stack.append(op_stack.pop())
                op_stack.append(char)
        while op_stack:
            self.postfix_stack.append(op_stack.pop())

    @staticmethod
    def is_operator(c):
        return c in {'+', '-', '*', '/', '(', ')', '%'}

    def compare(self, cur, peek):
        return self.operator_priority[cur] <= self.operator_priority[peek]

    @staticmethod
    def _calculate(first_value, second_value, current_op):
        first_value, second_value = Decimal(first_value), Decimal(second_value)
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
        # Remove spaces and return the cleaned expression
        return expression.replace(' ', '')

# Example usage
# expression_calculator = ExpressionCalculator()
# result = expression_calculator.calculate("2 + 3 * 4")
# print(result)  # Output: 14.0