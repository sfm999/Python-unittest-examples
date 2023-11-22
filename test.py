import unittest

from code.calculations import Calculations

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        calculations = Calculations(8, 2)
        # We are passing in the value gained, what we expect,
        # and the message to display if the assertion is false
        self.assertEqual(calculations.get_sum(), 10, 'The sum is wrong')

    def test_diff(self):
        calculations = Calculations(8, 2)
        self.assertEqual(calculations.get_difference(), 6, 'The difference is wrong')

    def test_product(self):
        calculations = Calculations(8, 2)
        self.assertEqual(calculations.get_product(), 16, 'The product is wrong')

    def test_quotient(self):
        calculations = Calculations(8, 2)
        self.assertEqual(calculations.get_quotient(), 4, 'The quotient is wrong')

        

if __name__ == '__main__':
    unittest.main()