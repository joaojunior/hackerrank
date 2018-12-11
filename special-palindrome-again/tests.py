import unittest

from main import substr_count


class SubstrCountTest(unittest.TestCase):
    def test_sample_0_return_7(self):
        s = 'asasd'
        expected = 7
        self.assertEqual(expected, substr_count(s))

    def test_sample_1_return_10(self):
        s = 'abcbaba'
        expected = 10
        self.assertEqual(expected, substr_count(s))

    def test_sample_2_return_10(self):
        s = 'aaaa'
        expected = 10
        self.assertEqual(expected, substr_count(s))


if __name__ == '__main__':
    unittest.main()
