from single_number_iii import Solution


def test_example_1():
    nums = [1, 2, 1, 3, 2, 5]
    expected = [3, 5]

    assert expected == Solution().single_number(nums)


def test_example_2():
    nums = [-1, 0]
    expected = [-1, 0]

    assert expected == Solution().single_number(nums)


def test_example_3():
    nums = [0, 1]
    expected = [0, 1]

    assert expected == Solution().single_number(nums)
