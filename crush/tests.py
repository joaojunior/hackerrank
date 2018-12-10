import unittest

from main import crush


class TestCrush(unittest.TestCase):
    def test_sample_input_1_return_200(self):
        n = 5
        queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
        expected = 200
        self.assertEqual(expected, crush(n, queries))

    def test_sample_input_2_return_31(self):
        n = 10
        queries = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]
        expected = 31
        self.assertEqual(expected, crush(n, queries))


if __name__ == '__main__':
    unittest.main()
