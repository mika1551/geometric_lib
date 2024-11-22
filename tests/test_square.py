import unittest
from square import area, perimeter


class TestSquareFunctions(unittest.TestCase):
    def test_area(self):
        # Проверка корректных значений для площади
        self.assertAlmostEqual(area(1), 1)
        self.assertAlmostEqual(area(2), 4)
        self.assertAlmostEqual(area(5.5), 30.25)
        self.assertAlmostEqual(area(0.1), 0.01)

    def test_perimeter(self):
        # Проверка корректных значений для периметра
        self.assertAlmostEqual(perimeter(1), 4)
        self.assertAlmostEqual(perimeter(2), 8)
        self.assertAlmostEqual(perimeter(5.5), 22)
        self.assertAlmostEqual(perimeter(0.1), 0.4)


if __name__ == "__main__":
    unittest.main()
