import unittest

from main import alternating_characters


class AlternateCharactersTest(unittest.TestCase):
    def test_sample_0_return_3(self):
        s = 'AAAA'
        expected = 3
        self.assertEqual(expected, alternating_characters(s))

    def test_sample_1_return_4(self):
        s = 'BBBBB'
        expected = 4
        self.assertEqual(expected, alternating_characters(s))

    def test_sample_2_return_0(self):
        s = 'ABABABAB'
        expected = 0
        self.assertEqual(expected, alternating_characters(s))

    def test_sample_3_return_0(self):
        s = 'BABABA'
        expected = 0
        self.assertEqual(expected, alternating_characters(s))

    def test_sample_4_return_4(self):
        s = 'AAABBB'
        expected = 4
        self.assertEqual(expected, alternating_characters(s))


if __name__ == '__main__':
    unittest.main()
