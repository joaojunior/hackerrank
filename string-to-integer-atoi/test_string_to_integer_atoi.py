from string_to_integer_atoi import Solution


def test_example_1():
    s = '42'
    expected = 42
    assert expected == Solution().my_atoi(s)


def test_example_2():
    s = '   -42'
    expected = -42
    assert expected == Solution().my_atoi(s)


def test_example_3():
    s = '4193 with words'
    expected = 4193
    assert expected == Solution().my_atoi(s)


def test_example_4():
    s = 'words and 987'
    expected = 0
    assert expected == Solution().my_atoi(s)


def test_example_5():
    s = '-91283472332'
    expected = -2147483648
    assert expected == Solution().my_atoi(s)
