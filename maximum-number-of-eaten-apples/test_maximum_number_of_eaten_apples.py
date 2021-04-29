from maximum_number_of_eaten_apples import Solution


def test_example1():
    apples = [1, 2, 3, 5, 2]
    days = [3, 2, 1, 4, 2]
    assert 7 == Solution().eaten_apples(apples, days)


def test_example2():
    apples = [3, 0, 0, 0, 0, 2]
    days = [3, 0, 0, 0, 0, 2]
    assert 5 == Solution().eaten_apples(apples, days)
