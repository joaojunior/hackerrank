from combinations import Solution


def test_example1():
    n = 4
    k = 2
    result = [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
        [3, 4],
    ]
    assert result == Solution().combine(n, k)


def test_example2():
    n = 1
    k = 1
    result = [
        [1],
    ]
    assert result == Solution().combine(n, k)
