class Calculator:
    def __init__(self):
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y
        }

    def calculate(self, expression):
        operand_stack = []
        operator_stack = []
        num = ''
        for char in expression:
            if char.isdigit():
                num += char
            else:
                operand_stack.append(int(num))
                num = ''
                while operator_stack and self.precedence(operator_stack[-1]) >= self.precedence(char):
                    operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
                operator_stack.append(char)
        if num:
            operand_stack.append(int(num))
        while operator_stack:
            operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
        return operand_stack[0]

    def precedence(self, operator):
        if operator == '^':
            return 3
        elif operator in ['*', '/']:
            return 2
        elif operator in ['+', '-']:
            return 1
        else:
            return 0

    def apply_operator(self, operand_stack, operator_stack):
        operator = operator_stack.pop()
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        result = self.operators[operator](operand1, operand2)
        operand_stack.append(result)
        return operand_stack, operator_stack