from unique_paths import Solution


def test_example1():
    m = 3
    n = 7
    expected = 28

    assert expected == Solution().unique_paths(m, n)


def test_example2():
    m = 3
    n = 2
    expected = 3

    assert expected == Solution().unique_paths(m, n)


def test_example3():
    m = 7
    n = 3
    expected = 28

    assert expected == Solution().unique_paths(m, n)


def test_example4():
    m = 3
    n = 3
    expected = 6

    assert expected == Solution().unique_paths(m, n)
