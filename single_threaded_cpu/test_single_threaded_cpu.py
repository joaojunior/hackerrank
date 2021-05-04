from single_threaded_cpu import Solution


def test_example_1():
    tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
    result = [0, 2, 3, 1]
    assert result == Solution().get_order(tasks)


def test_example_2():
    tasks = [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]
    result = [4, 3, 2, 0, 1]
    assert result == Solution().get_order(tasks)
