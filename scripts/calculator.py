import sys
sys.path.append('..')

from models.calculator import Calculator

calculator = Calculator()

input_string = input('--->')

calculator.set_raw_input(input_string)
calculator.calculate()

print(calculator.get_answer())

