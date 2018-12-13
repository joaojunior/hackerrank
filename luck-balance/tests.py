import unittest

from main import luck_balance


class LuckBalance(unittest.TestCase):
    def test_sample_0(self):
        k = 3
        contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
        expected = 29
        self.assertEqual(expected, luck_balance(k, contests))


if __name__ == '__main__':
    unittest.main()
