import unittest
from math import isclose
from triangle import area, perimeter


class TestTriangleFunctions(unittest.TestCase):
    def test_area_valid_triangle(self):
        """Проверка площади для валидных треугольников."""
        test_cases = [
            ((3, 4, 5), 6.0),
            ((6, 8, 10), 24.0),
            ((7, 24, 25), 84.0),
        ]
        for sides, expected in test_cases:
            with self.subTest(sides=sides):
                self.assertTrue(isclose(area(*sides), expected, rel_tol=1e-9))

    def test_area_degenerate_triangle(self):
        """Проверка площади для вырожденных треугольников."""
        test_cases = [
            ((1, 1, 2), 0.0),
            ((2, 3, 5), 0.0),
        ]
        for sides, expected in test_cases:
            with self.subTest(sides=sides):
                self.assertTrue(isclose(area(*sides), expected, rel_tol=1e-9))

    def test_area_invalid_triangle(self):
        """Проверка ошибок для невалидных треугольников."""
        invalid_cases = [
            (1, 1, 3),
            (0, 4, 5),
            (-3, 4, 5),
        ]
        for sides in invalid_cases:
            with self.subTest(sides=sides):
                with self.assertRaises(ValueError):
                    area(*sides)

    def test_perimeter_valid_triangle(self):
        """Проверка периметра для валидных треугольников."""
        test_cases = [
            ((3, 4, 5), 12),
            ((6, 8, 10), 24),
            ((7, 24, 25), 56),
        ]
        for sides, expected in test_cases:
            with self.subTest(sides=sides):
                self.assertEqual(perimeter(*sides), expected)

    def test_perimeter_invalid_inputs(self):
        """Проверка ошибок для невалидных входных данных."""
        invalid_cases = [
            (0, 4, 5),
            (-3, 4, 5),
            (1, 1, 3),
        ]
        for sides in invalid_cases:
            with self.subTest(sides=sides):
                with self.assertRaises(ValueError):
                    perimeter(*sides)

    def test_perimeter_degenerate_triangle(self):
        """Проверка периметра для вырожденных треугольников."""
        test_cases = [
            ((1, 1, 2), 4),
            ((2, 3, 5), 10),
        ]
        for sides, expected in test_cases:
            with self.subTest(sides=sides):
                self.assertEqual(perimeter(*sides), expected)


if __name__ == "__main__":
    unittest.main()
