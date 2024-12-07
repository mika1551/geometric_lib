import unittest
from square import area, perimeter


class TestSquareFunctions(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(0.1), 0.01, places=10)
        self.assertAlmostEqual(area(5), 25, places=10)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(0.1), 0.4, places=10)
        self.assertAlmostEqual(perimeter(5), 20, places=10)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_zero_side_area(self):
        self.assertEqual(area(0), 0)

    def test_zero_side_perimeter(self):
        self.assertEqual(perimeter(0), 0)

    def test_large_side(self):
        self.assertAlmostEqual(area(1e6), 1e12, places=10)
        self.assertAlmostEqual(perimeter(1e6), 4e6, places=10)


if __name__ == '__main__':
    unittest.main()
