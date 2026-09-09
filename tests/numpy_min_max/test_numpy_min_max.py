import unittest
import numpy

from src.numpy_min_max.util import find_max_after_min


class TestQuestion10(unittest.TestCase):

    def test_sample(self):
        array = numpy.array([
            [2, 5],
            [3, 7],
            [1, 3],
            [4, 0]
        ])

        self.assertEqual(find_max_after_min(array), 3)

    def test_second_case(self):
        array = numpy.array([
            [10, 20, 30],
            [5, 15, 25],
            [8, 12, 18]
        ])

        self.assertEqual(find_max_after_min(array), 10)


if __name__ == "__main__":
    unittest.main()