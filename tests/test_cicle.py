import unittest
from math import pi
from circle import area, perimeter


class TestCircleFunctions(unittest.TestCase):
    def test_area(self):
        """Проверка вычисления площади круга для различных радиусов."""
        test_cases = [
            (1, pi),
            (2, 4 * pi),
            (0, 0),
            (5.5, pi * 5.5**2),
            (0.1, pi * 0.1**2),
        ]
        for radius, expected in test_cases:
            with self.subTest(radius=radius):
                self.assertAlmostEqual(area(radius), expected)

    def test_perimeter(self):
        """Проверка вычисления периметра круга для различных радиусов."""
        test_cases = [
            (1, 2 * pi),
            (2, 4 * pi),
            (0, 0),
            (5.5, 2 * pi * 5.5),
            (0.1, 2 * pi * 0.1),
        ]
        for radius, expected in test_cases:
            with self.subTest(radius=radius):
                self.assertAlmostEqual(perimeter(radius), expected)


if __name__ == "__main__":
    unittest.main()
