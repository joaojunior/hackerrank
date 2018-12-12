import unittest

from main import riddle


class RiddleTest(unittest.TestCase):
    def test_example_input(self):
        array = [6, 3, 5, 1, 12]
        expected = [12, 3, 3, 1, 1]
        self.assertEqual(expected, riddle(array))

    def test_sample_0(self):
        array = [2, 6, 1, 12]
        expected = [12, 2, 1, 1]
        self.assertEqual(expected, riddle(array))

    def test_sample_1(self):
        array = [1, 2, 3, 5, 1, 13, 3]
        expected = [13, 3, 2, 1, 1, 1, 1]
        self.assertEqual(expected, riddle(array))

    def test_sample_2(self):
        array = [3, 5, 4, 7, 6, 2]
        expected = [7, 6, 4, 4, 3, 2]
        self.assertEqual(expected, riddle(array))


if __name__ == '__main__':
    unittest.main()
