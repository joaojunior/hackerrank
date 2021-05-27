from number_of_provinces import Solution


def test_example_1():
    is_connected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    expected = 2

    assert expected == Solution().find_circle_num(is_connected)


def test_example_2():
    is_connected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    expected = 3

    assert expected == Solution().find_circle_num(is_connected)
