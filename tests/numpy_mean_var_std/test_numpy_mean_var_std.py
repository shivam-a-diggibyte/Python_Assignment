import unittest
import numpy

from src.numpy_mean_var_std.util import calculate_values

class TestMeanVarStd(unittest.TestCase):

    def test_first_case(self):
        array = numpy.array([
            [1, 2],
            [3, 4]
        ])

        mean, var, std = calculate_values(array)

        self.assertEqual(mean.tolist(), [1.5, 3.5])
        self.assertEqual(var.tolist(), [1.0, 1.0])
        self.assertAlmostEqual(std, 1.11803398875)

    def test_second_case(self):
        array = numpy.array([
            [2, 4],
            [6, 8]
        ])

        mean, var, std = calculate_values(array)

        self.assertEqual(mean.tolist(), [3.0, 7.0])
        self.assertEqual(var.tolist(), [4.0, 4.0])
        self.assertAlmostEqual(std, 2.2360679775)

if __name__ == "__main__":
    unittest.main()