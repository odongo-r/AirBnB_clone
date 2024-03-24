# tests/test_num_factorial.py

import unittest
from num_factorial import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial_with_zero(self):
        result = factorial(0)
        self.assertEqual(result, 1)

    def test_factorial_with_positive_number(self):
        result = factorial(5)
        self.assertEqual(result, 120)

    def test_factorial_with_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()

