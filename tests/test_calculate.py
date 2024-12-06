import unittest
from calculate import calc


class TestCalculate(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calc('+', 2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(calc('-', 5, 2), 3)

    def test_multiplication(self):
        self.assertEqual(calc('*', 3, 4), 12)

    def test_division(self):
        self.assertEqual(calc('/', 8, 2), 4)

    def test_invalid_function(self):
        with self.assertRaises(ValueError):
            calc('circle', 'volume', [1])

    def test_invalid_size_length(self):
        with self.assertRaises(ValueError):
            calc('circle', 'area', [1, 2])

    def test_invalid_triangle_sides(self):
        with self.assertRaises(ValueError):
            calc('triangle', 'area', [1, 2, 10])


if __name__ == '__main__':
    unittest.main()
