from palindrome_partitioning import Solution


def test_example_1():
    s = "aab"
    expected = [["a", "a", "b"], ["aa", "b"]]

    assert expected == Solution().partition(s)


def test_example_2():
    s = "a"
    expected = [["a"]]

    assert expected == Solution().partition(s)
