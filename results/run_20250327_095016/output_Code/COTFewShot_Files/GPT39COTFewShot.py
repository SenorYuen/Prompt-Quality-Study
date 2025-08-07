import re
from collections import deque
from decimal import Decimal


class ExpressionCalculator:
    def __init__(self):
        self.postfix_stack = deque()
        self.operat_priority = [0, 3, 2, 1, -1, 1, 0, 2]

    def calculate(self, expression):
        self.prepare(expression)
        calc_stack = deque()
        while self.postfix_stack:
            token = self.postfix_stack.popleft()
            if not self.is_operator(token):
                calc_stack.append(Decimal(token))
            else:
                second_value = calc_stack.pop()
                first_value = calc_stack.pop()
                result = self._calculate(first_value, second_value, token)
                calc_stack.append(result)
        return float(calc_stack.pop())

    def prepare(self, expression):
        expression = self.transform(expression)
        operator_stack = deque()
        i = 0
        while i < len(expression):
            if expression[i].isdigit() or expression[i] == '.':
                j = i
                while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                self.postfix_stack.append(expression[i:j])
                i = j
            elif self.is_operator(expression[i]):
                while (operator_stack and operator_stack[-1] != '(' and
                       self.compare(expression[i], operator_stack[-1])):
                    self.postfix_stack.append(operator_stack.pop())
                operator_stack.append(expression[i])
                i += 1
            elif expression[i] == '(':
                operator_stack.append(expression[i])
                i += 1
            elif expression[i] == ')':
                while operator_stack and operator_stack[-1] != '(':
                    self.postfix_stack.append(operator_stack.pop())
                operator_stack.pop()
                i += 1

        while operator_stack:
            self.postfix_stack.append(operator_stack.pop())

    @staticmethod
    def is_operator(c):
        return c in {'+', '-', '*', '/', '(', ')', '%'}

    def compare(self, cur, peek):
        cur_priority = self.operat_priority['+-*/()'.index(cur)]
        peek_priority = self.operat_priority['+-*/()'.index(peek)]
        return cur_priority <= peek_priority

    @staticmethod
    def _calculate(first_value, second_value, current_op):
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
        return re.sub(r'\s+', '', expression)