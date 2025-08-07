class Calculator:
    """
    This is a class for a calculator, capable of performing basic arithmetic calculations on numerical expressions using the operators +, -, *, /, and ^ (exponentiation).
    """

    def __init__(self):
        """
        Initialize the operations performed by the five operators '+', '-', '*', '/', '^'
        """
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y
        }

    def calculate(self, expression):
        """
        Calculate the value of a given expression
        :param expression: string, given expression
        :return: If successful, returns the value of the expression; otherwise, returns None
        """
        def parse_expression(expression):
            number = ''
            tokens = []
            for char in expression:
                if char.isdigit() or char == '.':
                    number += char
                else:
                    if number:
                        tokens.append(float(number))
                        number = ''
                    tokens.append(char)
            if number:
                tokens.append(float(number))
            return tokens

        operand_stack = []
        operator_stack = []

        def apply_operator():
            operator = operator_stack.pop()
            right_operand = operand_stack.pop()
            left_operand = operand_stack.pop()
            operand_stack.append(self.operators[operator](left_operand, right_operand))

        tokens = parse_expression(expression)

        for token in tokens:
            if isinstance(token, float):
                operand_stack.append(token)
            else:
                while (operator_stack and
                       self.precedence(operator_stack[-1]) >= self.precedence(token)):
                    apply_operator()
                operator_stack.append(token)

        while operator_stack:
            apply_operator()

        return operand_stack[0] if operand_stack else None

    def precedence(self, operator):
        """
        Returns the priority of the specified operator, where the higher the priority, the greater the assignment.
        :param operator: string, given operator
        :return: int, the priority of the given operator, otherwise return 0
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence.get(operator, 0)

    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operand stack, and store the results at the top of the operand stack
        :param operand_stack: list
        :param operator_stack: list
        :return: the updated operand_stack and operator_stack
        """
        operator = operator_stack.pop()
        right_operand = operand_stack.pop()
        left_operand = operand_stack.pop()
        operand_stack.append(self.operators[operator](left_operand, right_operand))
        return operand_stack, operator_stack