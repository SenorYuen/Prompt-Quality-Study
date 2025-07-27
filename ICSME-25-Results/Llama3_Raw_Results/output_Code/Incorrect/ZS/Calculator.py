# This is a class for a calculator, capable of performing basic arithmetic calculations on numerical expressions using the operators +, -, *, /, and ^ (exponentiation).
class Calculator:
    def __init__(self):
        # Initialize the operations performed by the five operators'+','-','*','/','^'
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else float('inf'),
            '^': lambda x, y: x ** y
        }

    def calculate(self, expression):
        # Split the expression into tokens (numbers and operators)
        tokens = self.tokenize(expression)
        
        # Initialize the operand stack and operator stack
        operand_stack = []
        operator_stack = []
        
        # Iterate over each token in the expression
        for token in tokens:
            # If the token is a number, push it onto the operand stack
            if token.replace('.', '', 1).isdigit():
                operand_stack.append(float(token))
            # If the token is an operator, apply the operators with higher or equal precedence
            elif token in self.operators:
                while (operator_stack and 
                       self.precedence(operator_stack[-1]) >= self.precedence(token)):
                    operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
                operator_stack.append(token)
        
        # Apply any remaining operators
        while operator_stack:
            operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
        
        # Return the final result
        return operand_stack[0] if operand_stack else None

    def precedence(self, operator):
        # Returns the priority of the specified operator
        precedence_map = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }
        return precedence_map.get(operator, 0)

    def apply_operator(self, operand_stack, operator_stack):
        # Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operator stack
        operator = operator_stack.pop()
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        result = self.operators[operator](operand1, operand2)
        operand_stack.append(result)
        return operand_stack, operator_stack

    def tokenize(self, expression):
        # Split the expression into tokens (numbers and operators)
        tokens = []
        current_token = ''
        for char in expression:
            if char.isspace():
                continue
            if char in self.operators:
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
                tokens.append(char)
            else:
                current_token += char
        if current_token:
            tokens.append(current_token)
        return tokens