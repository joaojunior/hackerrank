from evaluate_reverse_polish_notation import Solution


def test_example1():
    tokens = ["2", "1", "+", "3", "*"]
    expected = 9

    assert expected == Solution().eval_rpn(tokens)


def test_example2():
    tokens = ["4", "13", "5", "/", "+"]
    expected = 6

    assert expected == Solution().eval_rpn(tokens)


def test_example3():
    tokens = [
        "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"
    ]
    expected = 22

    assert expected == Solution().eval_rpn(tokens)
