import unittest


from main import activity_notifications


class ActivityNotificationsTest(unittest.TestCase):
    def test_sample_0_return_2(self):
        d = 5
        expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
        expected = 2
        self.assertEqual(expected, activity_notifications(expenditure, d))

    def test_sample_1_return_0(self):
        d = 4
        expenditure = [1, 2, 3, 4, 4]
        expected = 0
        self.assertEqual(expected, activity_notifications(expenditure, d))


if __name__ == '__main__':
    unittest.main()
