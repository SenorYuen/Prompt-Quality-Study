import re
from collections import deque
from decimal import Decimal


class ExpressionCalculator:
    def __init__(self):
        self.postfix_stack = deque()
        self.operat_priority = {'+': 0, '-': 3, '*': 2, '/': 1, '%': -1, '(': 1, ')': 0, '^': 2}

    def calculate(self, expression):
        self.prepare(expression)
        stack = deque()
        for token in self.postfix_stack:
            if token not in self.operat_priority:
                stack.append(Decimal(token))
            else:
                second_value = stack.pop()
                first_value = stack.pop()
                result = self._calculate(first_value, second_value, token)
                stack.append(result)
        return float(stack.pop())

    def prepare(self, expression):
        self.postfix_stack.clear()
        expression = self.transform(expression)
        operator_stack = deque()
        for token in expression:
            if token not in self.operat_priority:
                self.postfix_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack[-1] != '(':
                    self.postfix_stack.append(operator_stack.pop())
                operator_stack.pop()
            else:
                while (operator_stack and 
                       self.compare(token, operator_stack[-1]) and 
                       operator_stack[-1] != '('):
                    self.postfix_stack.append(operator_stack.pop())
                operator_stack.append(token)
        while operator_stack:
            self.postfix_stack.append(operator_stack.pop())

    @staticmethod
    def is_operator(c):
        return c in {'+', '-', '*', '/', '(', ')', '%', '^'}

    def compare(self, cur, peek):
        return self.operat_priority[cur] >= self.operat_priority[peek]

    @staticmethod
    def _calculate(first_value, second_value, current_op):
        if current_op == '+':
            return first_value + second_value
        elif current_op == '-':
            return first_value - second_value
        elif current_op == '*':
            return first_value * second_value
        elif current_op == '/':
            if second_value == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return first_value / second_value
        elif current_op == '%':
            if second_value == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return first_value % second_value
        elif current_op == '^':
            return first_value ** second_value

    @staticmethod
    def transform(expression):
        return re.sub(r'\s', '', expression)