import unittest

from src.piling_up.util import can_stack

class TestPilingUp(unittest.TestCase):

    def test_first_case(self):
        blocks = [4, 3, 2, 1, 3, 4]

        self.assertEqual(can_stack(blocks), "Yes")

    def test_second_case(self):
        blocks = [1, 3, 2]

        self.assertEqual(can_stack(blocks), "No")

    def test_third_case(self):
        blocks = [5, 4, 3, 2, 1]

        self.assertEqual(can_stack(blocks), "Yes")

if __name__ == "__main__":
    unittest.main()