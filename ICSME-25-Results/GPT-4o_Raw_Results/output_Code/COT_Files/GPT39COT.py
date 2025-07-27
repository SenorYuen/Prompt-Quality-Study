import re
from collections import deque
from decimal import Decimal

class ExpressionCalculator:
    def __init__(self):
        self.postfix_stack = deque()
        self.operat_priority = [0, 3, 2, 1, -1, 1, 0, 2]

    def calculate(self, expression):
        self.prepare(expression)
        calculation_stack = deque()
        for token in self.postfix_stack:
            if not self.is_operator(token):
                calculation_stack.append(token)
            else:
                second_value = calculation_stack.pop()
                first_value = calculation_stack.pop()
                result = self._calculate(first_value, second_value, token)
                calculation_stack.append(result)
        return float(calculation_stack.pop())

    def prepare(self, expression):
        expression = self.transform(expression)
        operator_stack = deque()
        self.postfix_stack.clear()
        for char in expression:
            if not self.is_operator(char):
                self.postfix_stack.append(char)
            else:
                while (operator_stack and operator_stack[-1] != '(' and
                       self.compare(char, operator_stack[-1])):
                    self.postfix_stack.append(operator_stack.pop())
                if char == ')':
                    operator_stack.pop()
                else:
                    operator_stack.append(char)
        while operator_stack:
            self.postfix_stack.append(operator_stack.pop())

    @staticmethod
    def is_operator(c):
        return c in {'+', '-', '*', '/', '(', ')', '%'}

    def compare(self, cur, peek):
        return self.operat_priority[ord(cur) - 40] <= self.operat_priority[ord(peek) - 40]

    @staticmethod
    def _calculate(first_value, second_value, current_op):
        first = Decimal(first_value)
        second = Decimal(second_value)
        if current_op == '+':
            return first + second
        elif current_op == '-':
            return first - second
        elif current_op == '*':
            return first * second
        elif current_op == '/':
            return first / second
        elif current_op == '%':
            return first % second

    @staticmethod
    def transform(expression):
        return re.sub(r'\s+', '', expression)