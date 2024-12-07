import unittest
import math
from circle import area, perimeter


class TestCircleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(1), 3.141592653589793, places=10)
        self.assertAlmostEqual(area(0), 0, places=10)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1), 6.283185307179586, places=10)
        self.assertAlmostEqual(perimeter(0), 0, places=10)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            area(-1)
        with self.assertRaises(ValueError):
            perimeter(-1)

    def test_large_radius(self):
        self.assertAlmostEqual(area(1e6), math.pi * (1e6) ** 2, places=10)
        self.assertAlmostEqual(perimeter(1e6), 2 * math.pi * 1e6, places=10)


if __name__ == '__main__':
    unittest.main()
