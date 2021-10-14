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


if __name__ == '__main__':
    unittest.main()
