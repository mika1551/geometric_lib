import unittest
from square import area, perimeter


class TestSquareFunctions(unittest.TestCase):
    def test_area(self):
        """Проверка вычисления площади квадрата для различных сторон."""
        test_cases = [
            (1, 1),
            (2, 4),
            (5.5, 30.25),
            (0.1, 0.01),
        ]
        for side, expected in test_cases:
            with self.subTest(side=side):
                self.assertAlmostEqual(area(side), expected)

    def test_perimeter(self):
        """Проверка вычисления периметра квадрата для различных сторон."""
        test_cases = [
            (1, 4),
            (2, 8),
            (5.5, 22),
            (0.1, 0.4),
        ]
        for side, expected in test_cases:
            with self.subTest(side=side):
                self.assertAlmostEqual(perimeter(side), expected)


if __name__ == "__main__":
    unittest.main()
