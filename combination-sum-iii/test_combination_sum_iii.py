from combination_sum_iii import Solution


def test_example1():
    n = 7
    k = 3
    expected = [[1, 2, 4]]
    assert expected == Solution().combination_sum_3(k, n)


def test_example2():
    n = 9
    k = 3
    expected = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    assert expected == Solution().combination_sum_3(k, n)


def test_example3():
    n = 1
    k = 4
    expected = []
    assert expected == Solution().combination_sum_3(k, n)


def test_example4():
    n = 2
    k = 3
    expected = []
    assert expected == Solution().combination_sum_3(k, n)


def test_example5():
    n = 45
    k = 9
    expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
    assert expected == Solution().combination_sum_3(k, n)
