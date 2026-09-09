import unittest
from src.lists.util import process_command


class TestQuestion1(unittest.TestCase):

    def test_commands(self):
        numbers = []

        process_command(numbers, "insert 0 5")
        process_command(numbers, "insert 1 10")
        process_command(numbers, "insert 0 6")

        self.assertEqual(numbers, [6, 5, 10])

    def test_list_operations(self):
        numbers = [6, 5, 10]

        process_command(numbers, "remove 6")
        process_command(numbers, "append 9")
        process_command(numbers, "append 1")
        process_command(numbers, "sort")

        self.assertEqual(numbers, [1, 5, 9, 10])

    def test_print(self):
        numbers = [1, 5, 9]
        self.assertEqual(process_command(numbers, "print"), [1, 5, 9])


if __name__ == "__main__":
    unittest.main()