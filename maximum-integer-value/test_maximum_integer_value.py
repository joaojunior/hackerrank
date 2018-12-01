import unittest

from maximum_integer_value import maximum_integer_value


class MaximumIntegerValue(unittest.TestCase):
    def test_pass_01230_return_9(self):
        expected = 9
        self.assertEqual(expected, maximum_integer_value('01230'))


if __name__ == '__main__':
    unittest.main()
