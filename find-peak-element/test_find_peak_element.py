from find_peak_element import Solution


def test_example1():
    nums = [1, 2, 3, 1]
    expected = 2

    assert expected == Solution().find_peak_element(nums)


def test_example2():
    nums = [1, 2, 1, 3, 5, 6, 4]
    expected = 1

    assert expected == Solution().find_peak_element(nums)
