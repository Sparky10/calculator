import unittest
import sys

sys.path.append('..')

from models.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_create(self):
        """
        Test we can create a calculator instance
        """
        calculator = Calculator()
        self.assertIsInstance( calculator, Calculator, "Could not create a calculator instance.")

    def test_set_raw_input(self):
        """
        Test we can set raw input in the calculator
        """
        calculator = Calculator()
        return_value = calculator.set_raw_input('foobar')
        self.assertEqual(return_value, 'foobar', "Could not set correct raw input value")

    def test_calculations(self):
        """
        Test calculations produce the expected answers
        """
        calculator = Calculator()
        raw_input = calculator.set_raw_input('5 + 3')
        calculator.calculate()
        self.assertEqual(calculator.get_answer(), 8, 'Calculated answer was incorrect for: ' + raw_input)


if __name__ == '__main__':
    unittest.main()
