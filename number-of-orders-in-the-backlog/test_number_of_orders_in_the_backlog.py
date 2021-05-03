from number_of_orders_in_the_backlog import Solution


def test_example_1():
    orders = [[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]
    assert 6 == Solution().get_number_of_backlog_orders(orders)


def test_example_2():
    orders = [[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]
    assert 999999984 == Solution().get_number_of_backlog_orders(orders)
