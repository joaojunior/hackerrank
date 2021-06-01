from number_of_operations_to_make_network_connected import Solution


def test_example_1():
    n = 4
    connections = [[0, 1], [0, 2], [1, 2]]
    expected = 1

    assert expected == Solution().make_connected(n, connections)


def test_example_2():
    n = 6
    connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
    expected = 2

    assert expected == Solution().make_connected(n, connections)


def test_example_3():
    n = 6
    connections = [[0, 1], [0, 2], [0, 3], [1, 2]]
    expected = -1

    assert expected == Solution().make_connected(n, connections)


def test_example_4():
    n = 5
    connections = [[0, 1], [0, 2], [3, 4], [2, 3]]
    expected = 0

    assert expected == Solution().make_connected(n, connections)
