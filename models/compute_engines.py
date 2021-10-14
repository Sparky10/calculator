class ComputeError(Exception):
    pass


class SimpleComputeEngine:
    """
    The simple compute engine expects integer, operator, integer delimited by a single space
    """
    
    def __init__(self):
        self._left_operand = None
        self._right_operand = None
        self._operator = None
        self._permitted_operators = ['+','-','*','/']

    def split_input_string(self, input_string):
        return input_string.split(' ')

    def parse_operands(self, left, right):
        # Check operands are integers, if not throw exception

        try:
            self._left_operand = int(left)
            self._right_operand = int(right)
        except:
            raise ComputeError('Operands were not integers')

    def parse_operator(self, operator):
        # Check operator is in the whitelist, if not throw exception

        if operator in self._permitted_operators:
            self._operator = operator
        else:
            raise ComputeError('An illegal operator was used: ', self._operator)

    def parse(self, input_string):
        results = self.split_input_string(input_string)

        # We must have operand, operator, operand.  So any count other than 3 is wrong and we throw exception
        if len(results) != 3:
            raise ComputeError('Incorrect element count')

        # Bubble any exceptions up the chain
        try:
            self.parse_operands(results[0], results[2])
            self.parse_operator(results[1])
        except ComputeError as err:
            raise ComputeError(err)

    def get_results(self):
        return { 'left_operand' : self._left_operand, 
                 'right_operand' : self._right_operand, 
                 'operator' : self._operator }

    def make_calculation(self):
        if self._operator == '+':
            return self._left_operand + self._right_operand
        elif self._operator == '-':
            return self._left_operand - self._right_operand 
        elif self._operator == '*':
            return self._left_operand * self._right_operand
        elif self._operator == '/':
            return self._left_operand / self._right_operand
        else:
            raise ComputeError('Unable to calculate for unknown operator ', self._operator)


class ComplexComputeEngine(SimpleComputeEngine):
    """
    The complex compute engine can handle float operands and adds power(**) and modulus(%) operators.  
    There is also no need to include spaces in the input formula.
    """
    def __init__(self):
        super().__init__() 

