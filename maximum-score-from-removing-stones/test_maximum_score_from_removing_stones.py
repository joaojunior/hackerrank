from maximum_score_from_removing_stones import Solution


def test_example_1():
    a = 2
    b = 4
    c = 6

    assert 6 == Solution().maximum_score(a, b, c)


def test_example_12():
    a = 4
    b = 4
    c = 6

    assert 7 == Solution().maximum_score(a, b, c)
