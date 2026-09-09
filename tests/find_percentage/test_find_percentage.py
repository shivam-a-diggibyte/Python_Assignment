import unittest
from src.find_percentage.util import find_average, get_student_average

class TestQuestion2(unittest.TestCase):

    def test_find_average(self):
        self.assertEqual(find_average([52, 56, 60]), 56)

    def test_student_average(self):
        records = {
            "Malika": [52, 56, 60],
            "Arjun": [70, 98, 63]
        }
        self.assertEqual(get_student_average(records, "Malika"), 56)

    def test_decimal_marks(self):
        records = {
            "Harsh": [25, 26.5, 28]
        }
        self.assertEqual(get_student_average(records, "Harsh"), 26.5)


if __name__ == "__main__":
    unittest.main()