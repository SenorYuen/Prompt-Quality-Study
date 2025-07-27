import re
from collections import deque
from decimal import Decimal

class ExpressionCalculator:
    def __init__(self):
        self.postfix_stack = deque()
        self.operat_priority = {'+': 3, '-': 2, '*': 1, '/': -1, '%': 1, '(': 0, ')': 2}

    def calculate(self, expression):
        self.postfix_stack = deque(self.prepare(expression))
        stack = []
        while self.postfix_stack:
            token = self.postfix_stack.popleft()
            if token not in self.operat_priority:
                stack.append(float(token))
            else:
                second_value = stack.pop()
                first_value = stack.pop()
                result = self._calculate(first_value, second_value, token)
                stack.append(result)
        return stack[0]

    def prepare(self, expression):
        expression = self.transform(expression)
        output = []
        operator_stack = []
        for token in expression:
            if token not in self.operat_priority:
                output.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()
            else:
                while operator_stack and operator_stack[-1] != '(' and self.compare(token, operator_stack[-1]):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
        while operator_stack:
            output.append(operator_stack.pop())
        return output

    @staticmethod
    def is_operator(c):
        return c in {'+', '-', '*', '/', '(', ')', '%'}

    def compare(self, cur, peek):
        return self.operat_priority[cur] <= self.operat_priority[peek]

    @staticmethod
    def _calculate(first_value, second_value, current_op):
        if current_op == '+':
            return first_value + second_value
        elif current_op == '-':
            return first_value - second_value
        elif current_op == '*':
            return first_value * second_value
        elif current_op == '/':
            if second_value != 0:
                return first_value / second_value
            else:
                raise ZeroDivisionError("Cannot divide by zero")
        elif current_op == '%':
            if second_value != 0:
                return first_value % second_value
            else:
                raise ZeroDivisionError("Cannot divide by zero")

    @staticmethod
    def transform(expression):
        return re.sub(r'\s', '', expression)