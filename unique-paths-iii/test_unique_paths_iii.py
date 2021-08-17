from unique_paths_iii import Solution


def test_example_1():
    grid = [
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 2, -1]
    ]
    expected = 2

    assert expected == Solution().unique_paths_III(grid)


def test_example_2():
    grid = [
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 2]
    ]
    expected = 4

    assert expected == Solution().unique_paths_III(grid)


def test_example_3():
    grid = [
        [0, 1],
        [2, 0]
    ]
    expected = 0

    assert expected == Solution().unique_paths_III(grid)
