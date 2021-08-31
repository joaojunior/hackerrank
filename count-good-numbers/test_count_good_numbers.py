from count_good_numbers import Solution


def test_example_1():
    n = 1
    expected = 5
    assert expected == Solution().count_good_numbers(n)


def test_example_2():
    n = 4
    expected = 400
    assert expected == Solution().count_good_numbers(n)


def test_example_3():
    n = 50
    expected = 564908303
    assert expected == Solution().count_good_numbers(n)
