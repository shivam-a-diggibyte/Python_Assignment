import unittest

from src.floor_ceil_rint.util import calculate_values

class TestQuestion9(unittest.TestCase):

    def test_array_values(self):
        arr = [1.1, 2.2, 3.3, 4.4, 5.5]

        floor_value, ceil_value, rint_value = calculate_values(arr)

        self.assertEqual(floor_value.tolist(), [1.0, 2.0, 3.0, 4.0, 5.0])
        self.assertEqual(ceil_value.tolist(), [2.0, 3.0, 4.0, 5.0, 6.0])
        self.assertEqual(rint_value.tolist(), [1.0, 2.0, 3.0, 4.0, 6.0])

    def test_array_values_2(self):
            arr = [1.3, 2.2, 3.3, 4.2, 5.5]
    
            floor_value, ceil_value, rint_value = calculate_values(arr)
    
            self.assertEqual(floor_value.tolist(), [1.0, 2.0, 3.0, 4.0, 5.0])
            self.assertEqual(ceil_value.tolist(), [2.0, 3.0, 4.0, 5.0, 6.0])
            self.assertEqual(rint_value.tolist(), [1.0, 2.0, 3.0, 4.0, 6.0])

if __name__ == "__main__":
    unittest.main()