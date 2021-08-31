from find_kth_bit_in_nth_binary_string import Solution


def test_example_1():
    n = 3
    k = 1
    expected = '0'

    assert expected == Solution().find_kth_bit(n, k)


def test_example_2():
    n = 4
    k = 11
    expected = '1'

    assert expected == Solution().find_kth_bit(n, k)


def test_example_3():
    n = 1
    k = 1
    expected = '0'

    assert expected == Solution().find_kth_bit(n, k)


def test_example_4():
    n = 2
    k = 3
    expected = '1'

    assert expected == Solution().find_kth_bit(n, k)
