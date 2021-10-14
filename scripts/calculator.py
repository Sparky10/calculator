import sys
sys.path.append('..')

from models.calculator import Calculator
from models.compute_engines import ComputeError

calculator = Calculator()
input_string = None

while True:

    input_string = input('--->')

    if input_string == 'exit':
        break
    if input_string == '':
        continue
    else:
        try:
            calculator.set_raw_input(input_string)
            calculator.calculate()
        except ComputeError as err:
            print(err)
        else:
            print(calculator.get_answer())

print('Goodbye!')

