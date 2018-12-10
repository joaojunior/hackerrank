import unittest

from main import crush


class TestCrush(unittest.TestCase):
    def test_sample_input_1_return_200(self):
        m = 3
        queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
        expected = 200
        self.assertEqual(expected, crush(m, queries))


if __name__ == '__main__':
    unittest.main()
