import unittest

from code.calculations import Calculations

def setUpModule():
    print(f'Running setUpModule from {__name__}')

def tearDownModule():
    print(f'Running tearDownModule from {__name__}')


class TestCalculations(unittest.TestCase):

    # Override unittest.TestCase setUpClass() method
    # Will only run once on class start instead of before every function
    @classmethod
    def setUpClass(self) -> None:
        self.calculations = Calculations(8, 2)
        print('RUNNING setUpClass METHOD.')
        print('You can use this method to perform actions only once and before any tests are run.')
        print('Great for expensive processes or dependencies your tests have!')
        print('If an exception is thrown during setUpClass, then the tests are not run and neither is the tearDownClass method.')
        print('If the exception is a SkipTest exception, then the module will be reported as having been skipped instead of as an error')
        # print('This module should run 4 tests but when I raise the SkipTest exception, it will skip the rest of this module!\n')
        # raise unittest.SkipTest

    @classmethod
    def tearDownClass(self) -> None:
        print('\nRUNNING tearDownClass METHOD.')
        print('You can use this method to destroy any resources that were created during test or setUpClass.')
        print('Always clean up!')

    def test_sum(self) -> None:
        # We are passing in the value gained, what we expect,
        # and the message to display if the assertion is false
        self.assertEqual(self.calculations.get_sum(), 10, 'The sum is wrong')

    def test_diff(self) -> None:
        self.assertEqual(self.calculations.get_difference(), 6, 'The difference is wrong')

    def test_product(self) -> None:
        self.assertEqual(self.calculations.get_product(), 16, 'The product is wrong')

    def test_quotient(self) -> None:
        self.assertEqual(self.calculations.get_quotient(), 4, 'The quotient is wrong')


if __name__ == '__main__':
    unittest.main()