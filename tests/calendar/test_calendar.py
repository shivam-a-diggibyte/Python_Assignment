import unittest
from src.calendar.util import find_day

class TestQuestion6(unittest.TestCase):

    def test_sample_date(self):
        self.assertEqual(find_day(8, 5, 2015), "WEDNESDAY")

    def test_another_date(self):
        self.assertEqual(find_day(1, 1, 2020), "WEDNESDAY")

    def test_new_year(self):
        self.assertEqual(find_day(1, 1, 2021), "FRIDAY")


if __name__ == "__main__":
    unittest.main()