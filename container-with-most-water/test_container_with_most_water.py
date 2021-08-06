from container_with_most_water import Solution


def test_example_1():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    expected = 49
    assert expected == Solution().max_area(height)


def test_example_2():
    height = [1, 1]

    expected = 1
    assert expected == Solution().max_area(height)


def test_example_3():
    height = [4, 3, 2, 1, 4]

    expected = 16
    assert expected == Solution().max_area(height)


def test_example_4():
    height = [1, 2, 1]

    expected = 2
    assert expected == Solution().max_area(height)
