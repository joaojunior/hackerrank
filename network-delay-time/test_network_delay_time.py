from network_delay_time import Solution


def test_example_1():
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2

    expected = 2
    assert expected == Solution().network_delay_time(times, n, k)


def test_example_2():
    times = [[1, 2, 1]]
    n = 2
    k = 1

    expected = 1
    assert expected == Solution().network_delay_time(times, n, k)


def test_example_3():
    times = [[1, 2, 1]]
    n = 2
    k = 2

    expected = -1
    assert expected == Solution().network_delay_time(times, n, k)


def test_example_4():
    times = [[1, 2, 1], [2, 3, 2], [1, 3, 4]]
    n = 3
    k = 1

    expected = 3
    assert expected == Solution().network_delay_time(times, n, k)
