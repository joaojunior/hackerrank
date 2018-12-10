import unittest

from main import check_magazine


class TestCheckMagazine(unittest.TestCase):
    def test_sample_0_return_yes(self):
        magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
        note = ['give', 'one', 'grand', 'today']
        self.assertEqual('Yes', check_magazine(magazine, note))

    def test_sample_1_return_yes(self):
        magazine = ['two', 'times', 'three', 'is', 'not', 'four']
        note = ['two', 'times', 'two', 'is', 'four']
        self.assertEqual('No', check_magazine(magazine, note))

    def test_sample_2_return_yes(self):
        magazine = ['ive', 'got', 'a', 'lovely', 'bunch', 'of', 'coconuts']
        note = ['ive', 'got', 'some', 'coconuts']
        self.assertEqual('No', check_magazine(magazine, note))


if __name__ == '__main__':
    unittest.main()
