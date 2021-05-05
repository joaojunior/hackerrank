from permutations import Solution


def test_example_1():
    nums = [1, 2, 3]
    result = sorted(
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    )

    assert result == sorted(Solution().permute(nums))


def test_example_2():
    nums = [0, 1]
    result = [[0, 1], [1, 0]]

    assert result == Solution().permute(nums)
