import unittest

from main import largest_fibonacci_subsequence


class TestLargestFibonacciSubsequence(unittest.TestCase):
    def test_case_example_1(self):
        array = [1, 4, 3, 9, 10, 13, 7]

        expected = [1, 3, 13]
        self.assertEqual(expected, largest_fibonacci_subsequence(array))

    def test_case_example_2(self):
        array = [0, 2, 8, 5, 2, 1, 4, 13, 23]

        expected = [0, 2, 8, 5, 2, 1, 13]
        self.assertEqual(expected, largest_fibonacci_subsequence(array))


if __name__ == '__main__':
    unittest.main()
