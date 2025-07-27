from collections import deque
from decimal import Decimal

class ExpressionCalculator:
    def __init__(self):
        # Initialize the expression calculator
        self.postfix_stack = deque()
        # Define operator precedence
        self.operat_priority = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '(': 0}

    def calculate(self, expression):
        # Convert infix expression to postfix notation
        postfix_expression = self.prepare(expression)
        
        # Evaluate the postfix expression
        stack = deque()
        for char in postfix_expression:
            if char not in self.operat_priority and char not in ['(', ')']:
                # If the character is a number, push it to the stack
                stack.append(Decimal(char))
            else:
                # If the character is an operator, pop two numbers from the stack, perform the operation, and push the result
                second_value = stack.pop()
                first_value = stack.pop()
                result = self._calculate(first_value, second_value, char)
                stack.append(result)
        
        # The final result is the only element left in the stack
        return stack[0]

    def prepare(self, expression):
        # Transform the infix expression to a format suitable for conversion
        expression = self.transform(expression)
        
        # Initialize an empty stack to store operators
        operator_stack = deque()
        
        # Initialize an empty string to store the postfix expression
        postfix_expression = ''
        
        # Iterate over each character in the expression
        for char in expression:
            if char not in self.operat_priority and char not in ['(', ')']:
                # If the character is a number, add it to the postfix expression
                postfix_expression += char + ' '
            elif char == '(':
                # If the character is an open parenthesis, push it to the operator stack
                operator_stack.append(char)
            elif char == ')':
                # If the character is a close parenthesis, pop operators from the stack and add them to the postfix expression until an open parenthesis is found
                while operator_stack[-1] != '(':
                    postfix_expression += operator_stack.pop() + ' '
                # Remove the open parenthesis from the stack
                operator_stack.pop()
            else:
                # If the character is an operator, pop operators from the stack and add them to the postfix expression until an operator with lower precedence is found
                while operator_stack and operator_stack[-1] != '(' and self.compare(char, operator_stack[-1]):
                    postfix_expression += operator_stack.pop() + ' '
                # Push the current operator to the stack
                operator_stack.append(char)
        
        # Pop any remaining operators from the stack and add them to the postfix expression
        while operator_stack:
            postfix_expression += operator_stack.pop() + ' '
        
        return postfix_expression.strip()

    @staticmethod
    def is_operator(c):
        # Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        return c in {'+', '-', '*', '/', '(', ')', '%'}

    def compare(self, cur, peek):
        # Compare the precedence of two operators
        return self.operat_priority[cur] >= self.operat_priority[peek]

    @staticmethod
    def _calculate(first_value, second_value, current_op):
        # Perform the mathematical calculation based on the given operands and operator
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

    @staticmethod
    def transform(expression):
        # Transform the infix expression to a format suitable for conversion
        return expression.replace(' ', '')