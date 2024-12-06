import unittest
from shapes.square import area, perimeter

class TestSquareFunctions(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(1), 1)
        self.assertEqual(area(2), 4)
        self.assertEqual(area(5.5), 30.25)
        self.assertEqual(area(0.1), 0.01)

    def test_perimeter(self):
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(5.5), 22)
        self.assertEqual(perimeter(0.1), 0.4)

if __name__ == "__main__":
    unittest.main()
