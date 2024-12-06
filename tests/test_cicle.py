import unittest
from circle import area, perimeter


class TestCircleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(1), 3.14159, places=5)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1), 6.28318, places=5)


if __name__ == '__main__':
    unittest.main()
