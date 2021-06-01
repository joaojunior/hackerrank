from longest_increasing_path_in_a_matrix import Solution


def test_example_1():
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    expected = 4

    assert expected == Solution().longest_increasing_path(matrix)


def test_example_2():
    matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    expected = 4

    assert expected == Solution().longest_increasing_path(matrix)


def test_example_3():
    matrix = [[1]]
    expected = 1

    assert expected == Solution().longest_increasing_path(matrix)
