from three_sum_closest import Solution


def test_example1():
    nums = [-1, 2, 1, -4]
    target = 1
    expected = 2

    assert expected == Solution().three_sum_closest(nums, target)


def test_example2():
    nums = [0, 0, 0]
    target = 1
    expected = 0

    assert expected == Solution().three_sum_closest(nums, target)
