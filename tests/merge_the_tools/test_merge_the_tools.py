import unittest
from src.merge_the_tools.util import create_unique_part

class TestMergeTools(unittest.TestCase):

    def test_duplicate_characters(self):
        self.assertEqual(create_unique_part("AAB"), "AB")

    def test_all_unique(self):
        self.assertEqual(create_unique_part("BCA"), "BCA")

    def test_multiple_duplicates(self):
        self.assertEqual(create_unique_part("DDE"), "DE")

if __name__ == "__main__":
    unittest.main()