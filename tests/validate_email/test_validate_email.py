import unittest

from src.validate_email.util import fun

class TestValidEmail(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(fun("lara@hackerrank.com"))

    def test_invalid_email(self):
        self.assertFalse(fun("lara@hackerrank.corporate"))

    def test_special_character(self):
        self.assertFalse(fun("lara!@hackerrank.com"))

    def test_valid_username(self):
        self.assertTrue(fun("brian-23@hackerrank.com"))

if __name__ == "__main__":
    unittest.main()