import unittest
from triangle import area, perimeter


class TestTriangleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(3, 4, 5), 6.0, places=10)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_invalid_triangle_sides(self):
        with self.assertRaises(ValueError):
            area(1, 1, 10)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            area(-3, 4, 5)

    def test_zero_side(self):
        with self.assertRaises(ValueError):
            perimeter(0, 4, 5)

    def test_invalid_triangle_inequality(self):
        with self.assertRaises(ValueError):
            area(1, 2, 3)

    def test_valid_triangle(self):
        self.assertEqual(perimeter(3, 4, 5), 12)


if __name__ == '__main__':
    unittest.main()
