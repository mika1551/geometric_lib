import unittest
from calculate import calc

class TestCalculate(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(calc('circle', 'area', [1]), 3.141592653589793, places=10)
        self.assertAlmostEqual(calc('circle', 'area', [2]), 12.566370614359172, places=10)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(calc('circle', 'perimeter', [1]), 6.283185307179586, places=10)
        self.assertAlmostEqual(calc('circle', 'perimeter', [2]), 12.566370614359172, places=10)

    def test_square_area(self):
        self.assertEqual(calc('square', 'area', [1]), 1)
        self.assertEqual(calc('square', 'area', [5]), 25)

    def test_square_perimeter(self):
        self.assertEqual(calc('square', 'perimeter', [1]), 4)
        self.assertEqual(calc('square', 'perimeter', [3]), 12)

    def test_triangle_area(self):
        self.assertAlmostEqual(calc('triangle', 'area', [3, 4, 5]), 6.0, places=10)
        self.assertAlmostEqual(calc('triangle', 'area', [7, 24, 25]), 84.0, places=10)

    def test_triangle_perimeter(self):
        self.assertEqual(calc('triangle', 'perimeter', [3, 4, 5]), 12)
        self.assertEqual(calc('triangle', 'perimeter', [7, 24, 25]), 56)

    def test_invalid_inputs(self):
        with self.assertRaises(AssertionError):
            calc('pentagon', 'area', [1])
        with self.assertRaises(AssertionError):
            calc('circle', 'volume', [1])
        with self.assertRaises(AssertionError):
            calc('square', 'area', [-1])
        with self.assertRaises(ValueError):
            calc('triangle', 'area', [1, 2, 10])

if __name__ == '__main__':
    unittest.main()
