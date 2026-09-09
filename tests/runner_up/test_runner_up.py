import unittest

from src.runner_up.util import find_runner_up


class TestQuestion3(unittest.TestCase):

    def test_runner_up(self):
        scores = [2, 3, 6, 6, 5]

        self.assertEqual(find_runner_up(scores), 5)

    def test_duplicate_scores(self):
        scores = [10, 10, 8, 8, 5]

        self.assertEqual(find_runner_up(scores), 8)

    def test_negative_scores(self):
        scores = [-1, -2, -3, -1]

        self.assertEqual(find_runner_up(scores), -2)


if __name__ == "__main__":
    unittest.main()