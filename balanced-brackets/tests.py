import unittest

from main import is_balanced


class IsBalancedTest(unittest.TestCase):
    def test_sample_input_0_return_yes(self):
        s = '{[()]}'
        expected = 'YES'
        self.assertEqual(expected, is_balanced(s))

    def test_sample_input_1_return_yes(self):
        s = '{[(])}'
        expected = 'NO'
        self.assertEqual(expected, is_balanced(s))

    def test_sample_input_2_return_yes(self):
        s = '{{[[(())]]}}'
        expected = 'YES'
        self.assertEqual(expected, is_balanced(s))


if __name__ == '__main__':
    unittest.main()
