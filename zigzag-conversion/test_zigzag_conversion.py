from zigzag_conversion import Solution


def test_example1():
    s = 'PAYPALISHIRING'
    num_rows = 3
    expected = 'PAHNAPLSIIGYIR'

    assert expected == Solution().convert(s, num_rows)


def test_example2():
    s = 'PAYPALISHIRING'
    num_rows = 4
    expected = 'PINALSIGYAHRPI'

    assert expected == Solution().convert(s, num_rows)


def test_example3():
    s = 'AB'
    num_rows = 1
    expected = 'AB'

    assert expected == Solution().convert(s, num_rows)
