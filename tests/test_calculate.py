import unittest
from calculate import calc
class TestCalculateFunctions(unittest.TestCase):
    def test_valid_calculations(self):
        self.assertEqual(calc('circle', 'area', [1]), 3.141592653589793)
        self.assertEqual(calc('square', 'area', [2]), 4)
        self.assertEqual(calc('triangle', 'perimeter', [3, 4, 5]), 12)
    
    def test_invalid_figure(self):
        with self.assertRaises(ValueError):
            calc('pentagon', 'area', [1])
    
    def test_invalid_function(self):
        with self.assertRaises(ValueError):
            calc('circle', 'volume', [1])
    
    def test_invalid_size_length(self):
        with self.assertRaises(ValueError):
            calc('circle', 'area', [1, 2])
    
    def test_negative_sizes(self):
        with self.assertRaises(ValueError):
            calc('square', 'area', [-1])
    
    def test_invalid_triangle_sides(self):
        with self.assertRaises(ValueError):
            calc('triangle', 'area', [1, 2, 10])

if __name__ == "__main__":
    unittest.main()
