class Calculator:
    """
    This is a class for a calculator, capable of performing basic arithmetic calculations on numerical expressions using the operators +, -, *, /, and ^ (exponentiation).
    """

    def __init__(self):
        """
        Initialize the operations performed by the five operators'+','-','*','/','^'
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
        :return:If successful, returns the value of the expression; otherwise, returns None
        """
        # Split the expression into numbers and operators
        tokens = self.tokenize(expression)
        
        # Initialize operand and operator stacks
        operand_stack = []
        operator_stack = []
        
        # Process each token
        for token in tokens:
            # If the token is a number, push it to the operand stack
            if isinstance(token, float):
                operand_stack.append(token)
            # If the token is an operator, apply operators with higher or equal precedence
            elif token in self.operators:
                while (operator_stack and 
                       self.precedence(operator_stack[-1]) >= self.precedence(token)):
                    operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
                operator_stack.append(token)
        
        # Apply any remaining operators
        while operator_stack:
            operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
        
        # The final result is the only element left in the operand stack
        return operand_stack[0]

    def precedence(self, operator):
        """
        Returns the priority of the specified operator, where the higher the priority, the greater the assignment. The priority of '^' is greater than '/' and '*', and the priority of '/' and '*' is greater than '+' and '-'
        :param operator: string, given operator
        :return: int, the priority of the given operator, otherwise return 0
        """
        # Define operator precedence
        precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }
        return precedence.get(operator, 0)

    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operator stack, and store the results at the top of the operator stack
        :param operand_stack:list
        :param operator_stack:list
        :return: the updated operand_stack and operator_stack
        """
        # Pop the operator and two operands from their respective stacks
        operator = operator_stack.pop()
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        
        # Apply the operator
        result = self.operators[operator](operand1, operand2)
        
        # Push the result back to the operand stack
        operand_stack.append(result)
        
        return operand_stack, operator_stack

    def tokenize(self, expression):
        """
        Split the expression into numbers and operators
        :param expression: string, given expression
        :return: list, tokens
        """
        tokens = []
        current_token = ""
        
        # Iterate over each character in the expression
        for char in expression:
            # If the character is a digit or a decimal point, add it to the current token
            if char.isdigit() or char == '.':
                current_token += char
            # If the character is an operator, add the current token to the list and reset the current token
            elif char in self.operators:
                if current_token:
                    tokens.append(float(current_token))
                    current_token = ""
                tokens.append(char)
        
        # Add the last token to the list
        if current_token:
            tokens.append(float(current_token))
        
        return tokens