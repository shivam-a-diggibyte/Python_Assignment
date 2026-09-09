import unittest

from src.iterables_and_iterators.util import calculate_probability

class TestProbability(unittest.TestCase):

    def test_sample(self):
        letters = ['a', 'a', 'c', 'd']

        result = calculate_probability(letters, 2)

        self.assertAlmostEqual(result, 0.8333, places=3)

    def test_no_a(self):
        letters = ['b', 'c', 'd', 'e']

        result = calculate_probability(letters, 2)

        self.assertEqual(result, 0.0)

    def test_all_a(self):
        letters = ['a', 'a', 'a', 'a']

        result = calculate_probability(letters, 2)

        self.assertEqual(result, 1.0)

if __name__ == "__main__":
    unittest.main()