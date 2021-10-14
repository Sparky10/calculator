import unittest
import sys

sys.path.append('..')

from models.calculator import Calculator
from models.compute_engines import SimpleComputeEngine
from models.compute_engines import ComplexComputeEngine
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
        Test for both Simple and Complex engines
        """
        simple_compute_engine = ComputeService().inject_compute_engine('simple')
        self.assertIsInstance(simple_compute_engine, SimpleComputeEngine, "Could not fetch simple engine from the compute service.")

        complex_compute_engine = ComputeService().inject_compute_engine('complex')
        self.assertIsInstance(complex_compute_engine, ComplexComputeEngine, "Could not fetch complex engine from the compute service.")


    def test_simple_engine_parse(self):
        """
        Test the simple engine can parse input and detect malformed requests
        Assume we are aiming for a simple 'operand operator operand' input delimited by spaces
        """
        simple_compute_engine = ComputeService().inject_compute_engine('simple')
        
        try:
            simple_compute_engine.parse('foo + 3')
        except ComputeError as err:
            self.assertTrue(True)
        else:
            self.assertTrue(False,'Operand parse error not caught')

        try:
            simple_compute_engine.parse('5 foo 3')
        except ComputeError as err:
            self.assertTrue(True)
        else:
            self.assertTrue(False,'Operator parse error not caught')

        try:
            simple_compute_engine.parse('5.3 * 2.6')
        except ComputeError as err:
            self.assertTrue(True)
        else:
            self.assertTrue(False,'Operator parse error for floats not caught by simple engine')

        try:
            simple_compute_engine.parse('5 + 3')
        except ComputeError as err:
            self.assertTrue(False,'Simple compute engine could not parse well formed input')
        else:
            self.assertTrue(True)



    def test_complex_engine_parse(self):
        """
        Test the complex engine can parse input and detect malformed requests
        The complex engine adds power(^) and modulus(%) operators and can deal with floats and does not need space delimiters
        """
        complex_compute_engine = ComputeService().inject_compute_engine('simple')
        
        try:
            complex_compute_engine.parse('foo + 3')
        except ComputeError as err:
            self.assertTrue(True)
        else:
            self.assertTrue(False,'Operand parse error not caught')

        try:
            complex_compute_engine.parse('5 foo 3')
        except ComputeError as err:
            self.assertTrue(True)
        else:
            self.assertTrue(False,'Operator parse error not caught')

        try:
            complex_compute_engine.parse('5.3 * 2.6')
        except ComputeError as err:
            self.assertTrue(False, 'Complex engine unable to parse floats')
        else:
            self.assertTrue(True)

        try:
            complex_compute_engine.parse('5 ^ 3')
        except ComputeError as err:
            self.assertTrue(False,'Simple compute engine could not parse well formed input')
        else:
            self.assertTrue(True)






    def test_parse_results(self):
        """
        Test the engine parses input and correctly records operands and operators so they can be used in calculations
        """
        compute_engine = ComputeService().inject_compute_engine()
        
        try:
            compute_engine.parse('5 + 3')
        except ComputeError as err:
            print('Boom!', err)
        else:
            parsed_data = compute_engine.get_results()

            self.assertEqual(parsed_data['left_operand'], 5, "Could not parse left operand correctly")
            self.assertEqual(parsed_data['right_operand'], 3, "Could not parse right operand correctly")
            self.assertEqual(parsed_data['operator'], '+', "Could not parse operator correctly")






if __name__ == '__main__':
    unittest.main()
