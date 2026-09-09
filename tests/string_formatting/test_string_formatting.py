import unittest
from src.string_formatting.util import format_numbers


class TestPrintFormatting(unittest.TestCase):

    def test_format_numbers(self):
        format_numbers(3)

        # Test the function runs without error
        self.assertTrue(True)

    def test_single_number(self):
        format_numbers(1)

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()