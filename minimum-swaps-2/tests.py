import unittest

from main import minimum_swaps


class TestMinimumSwaps(unittest.TestCase):
    def test_pass_4_3_1_2_return_3(self):
        array = [4, 3, 1, 2]
        expected = 3
        self.assertEqual(expected, minimum_swaps(array))

    def test_pass_2_3_4_1_5_return_3(self):
        array = [2, 3, 4, 1, 5]
        expected = 3
        self.assertEqual(expected, minimum_swaps(array))

    def test_pass_1_3_5_2_4_6_7_return_3(self):
        array = [1, 3, 5, 2, 4, 6, 7]
        expected = 3
        self.assertEqual(expected, minimum_swaps(array))


if __name__ == '__main__':
    unittest.main()
