import unittest

from main import common_child


class TestCommonChild(unittest.TestCase):
    def test_sample_0_return_2(self):
        s1 = 'HARRY'
        s2 = 'SALLY'
        expected = 2
        self.assertEqual(expected, common_child(s1, s2))

    def test_sample_1_return_0(self):
        s1 = 'AA'
        s2 = 'BB'
        expected = 0
        self.assertEqual(expected, common_child(s1, s2))

    def test_sample_2_return_3(self):
        s1 = 'SHINCHAN'
        s2 = 'NOHARAAA'
        expected = 3
        self.assertEqual(expected, common_child(s1, s2))

    def test_sample_3_return_3(self):
        s1 = 'ABCDEF'
        s2 = 'FBDAMN'
        expected = 2
        self.assertEqual(expected, common_child(s1, s2))

    def test_sample_s1_equal_s2_return_size_s1(self):
        s1 = 'ABCD'
        s2 = 'ABCD'
        expected = len(s1)
        self.assertEqual(expected, common_child(s1, s2))


if __name__ == '__main__':
    unittest.main()
