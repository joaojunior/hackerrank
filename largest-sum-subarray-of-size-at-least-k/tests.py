import unittest

from main import largest_sum_subarray_of_size_at_least_k


class TestLargestSumSubarrayOfSizeAtLeastK(unittest.TestCase):
    def test_first_example_case(self):
        array = [-4, -2, 1, -3]
        k = 2

        expected = -1
        result = largest_sum_subarray_of_size_at_least_k(array, k)
        self.assertEqual(expected, result)

    def test_second_example_case(self):
        array = [1, 1, 1, 1, 1, 1]
        k = 2

        expected = 6
        result = largest_sum_subarray_of_size_at_least_k(array, k)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
