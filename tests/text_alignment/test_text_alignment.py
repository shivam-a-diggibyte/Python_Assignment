import unittest
from src.text_alignment.util import create_logo


class TestQuestion5(unittest.TestCase):

    def test_logo(self):
        create_logo(5)
        self.assertTrue(True)

    def test_small_logo(self):
        create_logo(3)
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()