from find_the_winner_of_the_circular_game import Solution


def test_example_1():
    n = 5
    k = 2
    expected = 3
    assert expected == Solution().find_the_winner(n, k)


def test_example_2():
    n = 6
    k = 5
    expected = 1
    assert expected == Solution().find_the_winner(n, k)
