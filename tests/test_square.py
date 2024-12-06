import unittest
from square import area, perimeter


class TestSquareFunctions(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4), 16)

    def test_perimeter(self):
        self.assertEqual(perimeter(4), 16)


if __name__ == '__main__':
    unittest.main()
