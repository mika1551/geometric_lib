import unittest
from math import pi
from circle import area, perimeter


class TestCircleFunctions(unittest.TestCase):
    def test_area(self):
        # Проверка площади круга для различных радиусов
        self.assertAlmostEqual(area(1), pi)
        self.assertAlmostEqual(area(2), 4 * pi)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(5.5), pi * 5.5 * 5.5)
        self.assertAlmostEqual(area(0.1), pi * 0.1 * 0.1)

    def test_perimeter(self):
        # Проверка периметра круга для различных радиусов
        self.assertAlmostEqual(perimeter(1), 2 * pi)
        self.assertAlmostEqual(perimeter(2), 4 * pi)
        self.assertAlmostEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(5.5), 2 * pi * 5.5)
        self.assertAlmostEqual(perimeter(0.1), 2 * pi * 0.1)


if __name__ == "__main__":
    unittest.main()
