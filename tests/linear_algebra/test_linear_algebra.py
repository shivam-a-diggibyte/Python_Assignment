import unittest
import numpy

from src.linear_algebra.util import find_determinant

class TestNumpyDeterminant(unittest.TestCase):

    def test_first_matrix(self):
        matrix = numpy.array([
            [1.1, 1.1],
            [1.1, 1.1]
        ])

        self.assertEqual(round(find_determinant(matrix), 2), 0.0)

    def test_second_matrix(self):
        matrix = numpy.array([
            [1, 2],
            [2, 1]
        ])

        self.assertEqual(round(find_determinant(matrix), 2), -3.0)

if __name__ == "__main__":
    unittest.main()