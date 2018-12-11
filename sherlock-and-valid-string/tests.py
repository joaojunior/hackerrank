import unittest

from main import is_valid


class IsValidTest(unittest.TestCase):
    def test_sample_0_return_no(self):
        s = 'aabbcd'
        expected = 'NO'
        self.assertEqual(expected, is_valid(s))

    def test_sample_1_return_no(self):
        s = 'aabbccddeefghi'
        expected = 'NO'
        self.assertEqual(expected, is_valid(s))

    def test_sample_2_return_yes(self):
        s = 'abcdefghhgfedecba'
        expected = 'YES'
        self.assertEqual(expected, is_valid(s))

    def test_sample_3_return_yes(self):
        s = 'a'
        expected = 'YES'
        self.assertEqual(expected, is_valid(s))

    def test_sample_4_return_yes(self):
        s = 'abcdd'
        expected = 'YES'
        self.assertEqual(expected, is_valid(s))

    def test_sample_5_return_yes(self):
        s = 'abcd'
        expected = 'YES'
        self.assertEqual(expected, is_valid(s))

    def test_sample_6_return_no(self):
        s = 'aaaabb'
        expected = 'NO'
        self.assertEqual(expected, is_valid(s))

    def test_sample_7_return_yes(self):
        s = 'abbac'
        expected = 'YES'
        self.assertEqual(expected, is_valid(s))

    def test_sample_8_return_no(self):
        s = 'abbacd'
        expected = 'NO'
        self.assertEqual(expected, is_valid(s))

    def test_sample_9_return_yes(self):
        s = 'ab'
        expected = 'YES'
        self.assertEqual(expected, is_valid(s))

    def test_sample_10_return_yes(self):
        s = 'aaabbbc'
        expected = 'YES'
        self.assertEqual(expected, is_valid(s))


if __name__ == '__main__':
    unittest.main()
