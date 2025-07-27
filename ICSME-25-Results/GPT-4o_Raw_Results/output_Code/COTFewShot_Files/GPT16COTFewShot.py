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
        def precedence(operator):
            if operator in ('+', '-'):
                return 1
            if operator in ('*', '/'):
                return 2
            if operator == '^':
                return 3
            return 0

        def apply_operator(operand_stack, operator_stack):
            operator = operator_stack.pop()
            right = operand_stack.pop()
            left = operand_stack.pop()
            operand_stack.append(self.operators[operator](left, right))

        operand_stack = []
        operator_stack = []
        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                num = 0
                while i < len(expression) and expression[i].isdigit():
                    num = num * 10 + int(expression[i])
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

        return operand_stack[0]