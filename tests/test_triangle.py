import unittest
from triangle import area, perimeter
class TestTriangleFunctions(unittest.TestCase):
    def test_area_valid_triangle(self):
        self.assertAlmostEqual(area(3, 4, 5), 6.0)
        self.assertAlmostEqual(area(6, 8, 10), 24.0)

    def test_area_invalid_triangle(self):
        with self.assertRaises(ValueError):
            area(1, 1, 3)

    def test_perimeter_valid_triangle(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(6, 8, 10), 24)

    def test_perimeter_invalid_triangle(self):
        with self.assertRaises(ValueError):
            perimeter(1, 1, 3)

if __name__ == "__main__":
    unittest.main()
