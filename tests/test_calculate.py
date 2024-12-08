import unittest
from calculate import calc


class TestCalculate(unittest.TestCase):
    def test_calc_circle(self):
        self.assertAlmostEqual(calc('circle', 'area', [1]), 3.141592653589793, places=10)
        self.assertAlmostEqual(calc('circle', 'perimeter', [1]), 6.283185307179586, places=10)

    def test_calc_square(self):
        self.assertEqual(calc('square', 'area', [2]), 4)
        self.assertEqual(calc('square', 'perimeter', [2]), 8)

    def test_calc_triangle(self):
        self.assertAlmostEqual(calc('triangle', 'area', [3, 4, 5]), 6.0, places=10)
        self.assertEqual(calc('triangle', 'perimeter', [3, 4, 5]), 12)

    def test_invalid_figure(self):
        with self.assertRaises(ValueError):
            calc('pentagon', 'area', [1])

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
