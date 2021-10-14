import unittest
import sys

sys.path.append('..')

from models.calculator import Calculator
from models.compute_engines import ComputeEngine
from models.compute_engines import ComputeError
from services.compute_service import ComputeService

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


class TestEngine(unittest.TestCase):

    def test_inject_compute_engine(self):
        """
        Test that a compute service can return a compute engine to carry out the work
        """
        compute_engine = ComputeService().inject_compute_engine()
        self.assertIsInstance(compute_engine, ComputeEngine, "Could not fetch engine from the compute service.")

    def test_parse(self):
        """
        Test we can parse input and detect malformed requests
        Assume we are aiming for a simple 'operand operator operand' input delimited by spaces
        """
        compute_engine = ComputeService().inject_compute_engine()
        
        try:
            compute_engine.parse('foo + 3')
        except ComputeError as err:
            self.assertTrue(True)
        else:
            self.assertTrue(False,'Operand parse error not caught')

        try:
            compute_engine.parse('5 foo 3')
        except ComputeError as err:
            self.assertTrue(True)
        else:
            self.assertTrue(False,'Operator parse error not caught')








if __name__ == '__main__':
    unittest.main()
