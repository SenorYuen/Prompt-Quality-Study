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
        def precedence(op):
            if op == '+' or op == '-':
                return 1
            if op == '*' or op == '/':
                return 2
            if op == '^':
                return 3
            return 0

        def apply_operator(operand_stack, operator_stack):
            right = operand_stack.pop()
            left = operand_stack.pop()
            op = operator_stack.pop()
            operand_stack.append(self.operators[op](left, right))

        operand_stack = []
        operator_stack = []
        i = 0
        while i < len(expression):
            if expression[i].isdigit() or expression[i] == '.':
                num = ''
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num += expression[i]
                    i += 1
                operand_stack.append(float(num))
                i -= 1
            elif expression[i] in self.operators:
                while (operator_stack and
                       precedence(operator_stack[-1]) >= precedence(expression[i])):
                    apply_operator(operand_stack, operator_stack)
                operator_stack.append(expression[i])
            i += 1

        while operator_stack:
            apply_operator(operand_stack, operator_stack)

        return operand_stack[0] if operand_stack else None

    def precedence(self, operator):
        if operator in self.operators:
            return {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}[operator]
        return 0

    def apply_operator(self, operand_stack, operator_stack):
        right = operand_stack.pop()
        left = operand_stack.pop()
        op = operator_stack.pop()
        operand_stack.append(self.operators[op](left, right))
        return operand_stack, operator_stack