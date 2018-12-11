import unittest

from main import make_anagrams


class MakeAnagramsTest(unittest.TestCase):
    def test_sample_0_return_4(self):
        a = 'cde'
        b = 'abc'
        expected = 4
        self.assertEqual(expected, make_anagrams(a, b))


if __name__ == '__main__':
    unittest.main()
