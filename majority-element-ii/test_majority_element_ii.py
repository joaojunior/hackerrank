from majority_element_ii import Solution


def test_example_1():
    nums = [3, 2, 3]
    expected = [3]

    assert expected == Solution().majority_element(nums)


def test_example_2():
    nums = [1]
    expected = [1]

    assert expected == Solution().majority_element(nums)


def test_example_3():
    nums = [1, 2]
    expected = [1, 2]

    assert expected == Solution().majority_element(nums)
