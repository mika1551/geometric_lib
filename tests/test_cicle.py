import unittest
from shapes.circle import area, perimeter
from math import pi

class TestCircleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(1), pi)
        self.assertAlmostEqual(area(2), 4 * pi)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(5.5), pi * 5.5 ** 2)
    
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1), 2 * pi)
        self.assertAlmostEqual(perimeter(2), 4 * pi)
        self.assertAlmostEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(5.5), 2 * pi * 5.5)

if __name__ == "__main__":
    unittest.main()
