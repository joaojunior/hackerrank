from minimum_path_sum import Solution


def test_example_1():
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    expected = 7

    assert expected == Solution().min_path_sum(grid)


def test_example_2():
    grid = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    expected = 12

    assert expected == Solution().min_path_sum(grid)
