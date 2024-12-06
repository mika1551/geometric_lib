import unittest
from calculate import calc

class TestCalculate(unittest.TestCase):
    def test_calc(self):
        self.assertEqual(calc('+', 2, 3), 5)
        self.assertEqual(calc('-', 2, 3), -1)
        self.assertEqual(calc('*', 2, 3), 6)
        self.assertAlmostEqual(calc('/', 3, 2), 1.5, places=10)
        with self.assertRaises(ValueError):
            calc('/', 3, 0)

if __name__ == '__main__':
    unittest.main()
