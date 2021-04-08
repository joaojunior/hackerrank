from solution import Solution


def test_example_1():
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    expected = 2
    assert expected == Solution().find_min_arrow_shots(points)


def test_example_2():
    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    expected = 4
    assert expected == Solution().find_min_arrow_shots(points)


def test_example_3():
    points = [[1, 2], [2, 3], [3, 4], [4, 5]]
    expected = 2
    assert expected == Solution().find_min_arrow_shots(points)


def test_empty_points():
    expected = 0
    assert expected == Solution().find_min_arrow_shots([])
