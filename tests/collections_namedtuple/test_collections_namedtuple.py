import unittest

from src.collections_namedtuple.util import calculate_average

class TestQuestion7(unittest.TestCase):

    def test_average_marks(self):
        headers = ["ID", "MARKS", "NAME", "CLASS"]

        students = [
            ["1", "97", "Raymond", "7"],
            ["2", "50", "Steven", "4"],
            ["3", "91", "Adrian", "9"],
            ["4", "72", "Stewart", "5"],
            ["5", "80", "Peter", "6"]
        ]

        result = calculate_average(headers, students)

        self.assertEqual(result, 78.0)

    def test_different_column_order(self):
        headers = ["MARKS", "CLASS", "NAME", "ID"]

        students = [
            ["92", "2", "Calum", "1"],
            ["82", "5", "Scott", "2"],
            ["94", "2", "Jason", "3"],
            ["55", "8", "Glenn", "4"],
            ["82", "2", "Fergus", "5"]
        ]

        result = calculate_average(headers, students)

        self.assertEqual(result, 81.0)

if __name__ == "__main__":
    unittest.main()