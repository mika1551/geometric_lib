import unittest
import math
from figures import area, perimeter


class TestTriangleFunctions(unittest.TestCase):
    def test_triangle_area(self):
        self.assertAlmostEqual(area('triangle', [3, 4, 5]), 6.0, places=10)

    def test_triangle_perimeter(self):
        self.assertEqual(perimeter('triangle', [3, 4, 5]), 12)

    def test_triangle_invalid_sides(self):
        with self.assertRaises(ValueError):
            area('triangle', [1, 1, 10])

    def test_triangle_negative_sides(self):
        with self.assertRaises(ValueError):
            area('triangle', [-3, 4, 5])

    def test_triangle_zero_side(self):
        with self.assertRaises(ValueError):
            perimeter('triangle', [0, 4, 5])


class TestCircleFunctions(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(area('circle', [3]), math.pi * 3 ** 2, places=10)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(perimeter('circle', [3]), 2 * math.pi * 3, places=10)

    def test_circle_negative_radius(self):
        with self.assertRaises(ValueError):
            area('circle', [-3])

    def test_circle_zero_radius(self):
        with self.assertRaises(ValueError):
            perimeter('circle', [0])


class TestSquareFunctions(unittest.TestCase):
    def test_square_area(self):
        self.assertEqual(area('square', [4]), 16)

    def test_square_perimeter(self):
        self.assertEqual(perimeter('square', [4]), 16)

    def test_square_negative_side(self):
        with self.assertRaises(ValueError):
            area('square', [-4])

    def test_square_zero_side(self):
        with self.assertRaises(ValueError):
            perimeter('square', [0])


if __name__ == '__main__':
    unittest.main()
