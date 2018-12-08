import unittest

from count_triplets import count_triplets


class TestCountTriplets(unittest.TestCase):
    def test_pass_array_1_2_2_4_r_2_return_2(self):
        array = [1, 2, 2, 4]
        expected = 2
        self.assertEqual(expected, count_triplets(array, 2))

    def test_pass_array_1_3_9_9_27_81_r_3_return_6(self):
        array = [1, 3, 9, 9, 27, 81]
        expected = 6
        self.assertEqual(expected, count_triplets(array, 3))

    def test_pass_array_1_5_5_25_125_r_5_return_4(self):
        array = [1, 5, 5, 25, 125]
        expected = 4
        self.assertEqual(expected, count_triplets(array, 5))


if __name__ == '__main__':
    unittest.main()
