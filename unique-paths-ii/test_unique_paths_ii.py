from unique_paths_ii import Solution


def test_example_1():
    obstacle_grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    expected = 2

    assert expected == Solution().unique_paths_with_obstacles(obstacle_grid)


def test_example_2():
    obstacle_grid = [
        [0, 1],
        [0, 0]
    ]
    expected = 1

    assert expected == Solution().unique_paths_with_obstacles(obstacle_grid)
