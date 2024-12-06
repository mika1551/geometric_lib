import unittest
from triangle import area, perimeter


class TestTriangleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(3, 4, 5), 6, places=5)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)


if __name__ == '__main__':
    unittest.main()
