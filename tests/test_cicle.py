import unittest
from circle import area, perimeter

class TestCircleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(1), 3.141592653589793, places=10)
        self.assertAlmostEqual(area(0), 0, places=10)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1), 6.283185307179586, places=10)
        self.assertAlmostEqual(perimeter(0), 0, places=10)

if __name__ == '__main__':
    unittest.main()
