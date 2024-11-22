import unittest
import triangle

class TestTriangleFunctions(unittest.TestCase):
    def test_area_valid_triangle(self):
        self.assertTrue(isclose(area(3, 4, 5), 6.0, rel_tol=1e-9))
        self.assertTrue(isclose(area(6, 8, 10), 24.0, rel_tol=1e-9))
        self.assertTrue(isclose(area(7, 24, 25), 84.0, rel_tol=1e-9))

    def test_area_degenerate_triangle(self):
        self.assertTrue(isclose(area(1, 1, 2), 0.0, rel_tol=1e-9))
        self.assertTrue(isclose(area(2, 3, 5), 0.0, rel_tol=1e-9))

    def test_area_invalid_triangle(self):
        with self.assertRaises(ValueError):
            area(1, 1, 3)
        with self.assertRaises(ValueError):
            area(0, 4, 5)
        with self.assertRaises(ValueError):
            area(-3, 4, 5)

    def test_perimeter_valid_triangle(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(6, 8, 10), 24)
        self.assertEqual(perimeter(7, 24, 25), 56)

    def test_perimeter_invalid_inputs(self):
        with self.assertRaises(ValueError):
            perimeter(0, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(1, 1, 3)

    def test_perimeter_degenerate_triangle(self):
        self.assertEqual(perimeter(1, 1, 2), 4)
        self.assertEqual(perimeter(2, 3, 5), 10)


if __name__ == "__main__":
    unittest.main()
