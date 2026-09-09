import unittest

from src.no_idea.util import calculate_happiness


class TestNoIdea(unittest.TestCase):

    def test_sample(self):
        array = [1, 5, 3]
        liked = {3, 1}
        disliked = {5, 7}

        self.assertEqual(calculate_happiness(array, liked, disliked), 1)

    def test_second_case(self):
        array = [1, 2, 3, 4, 5]
        liked = {1, 3}
        disliked = {2, 5}

        self.assertEqual(calculate_happiness(array, liked, disliked), 0)


if __name__ == "__main__":
    unittest.main()