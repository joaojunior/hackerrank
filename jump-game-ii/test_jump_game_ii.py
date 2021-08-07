from jump_game_ii import Solution


def test_example_1():
    nums = [2, 3, 1, 1, 4]
    expected = 2

    assert expected == Solution().jump(nums)


def test_example_2():
    nums = [2, 3, 0, 1, 4]
    expected = 2

    assert expected == Solution().jump(nums)
