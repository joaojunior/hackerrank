from cheapest_flights_within_k_stops import Solution


def test_example_1():
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1

    assert 200 == Solution().find_cheapest_price(n, flights, src, dst, k)


def test_example_2():
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0

    assert 500 == Solution().find_cheapest_price(n, flights, src, dst, k)


def test_example_solution_is_impossible():
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 2
    dst = 0
    k = 2

    assert -1 == Solution().find_cheapest_price(n, flights, src, dst, k)
