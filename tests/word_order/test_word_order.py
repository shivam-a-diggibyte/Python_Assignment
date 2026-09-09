import unittest

from src.word_order.util import count_words

class TestWordOrder(unittest.TestCase):

    def test_sample(self):
        words = ["bcdef", "abcdefg", "bcde", "bcdef"]

        result = count_words(words)

        self.assertEqual(result, (3, [2, 1, 1]))

    def test_repeated_words(self):
        words = ["apple", "banana", "apple", "apple", "banana"]

        result = count_words(words)

        self.assertEqual(result, (2, [3, 2]))

if __name__ == "__main__":
    unittest.main()