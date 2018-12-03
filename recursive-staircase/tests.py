import unittest

from main import recursive_staircase


class TestRecursiveStairCase(unittest.TestCase):
    def test_n_is_5_return_13(self):
        expected = 13
        self.assertEqual(expected, recursive_staircase(5))

    def test_n_is_1_return_1(self):
        expected = 1
        self.assertEqual(expected, recursive_staircase(1))

    def test_n_is_3_return_4(self):
        expected = 4
        self.assertEqual(expected, recursive_staircase(3))

    def test_n_is_7_return_44(self):
        expected = 44
        self.assertEqual(expected, recursive_staircase(7))


if __name__ == '__main__':
    unittest.main()
