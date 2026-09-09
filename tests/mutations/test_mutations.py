import unittest
from src.mutations.util import mutate_string

class TestMutateString(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(
            mutate_string("abracadabra", 5, "k"),
            "abrackdabra"
        )
    def test_first_character(self):
        self.assertEqual(
            mutate_string("hello", 0, "y"),
            "yello"
        )
    def test_last_character(self):
        self.assertEqual(
            mutate_string("hello", 4, "y"),
            "helly"
        )

if __name__ == "__main__":
    unittest.main()