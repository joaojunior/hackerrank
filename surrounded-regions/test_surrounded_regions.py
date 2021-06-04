from surrounded_regions import Solution


def test_example_1():
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    expected = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]
    ]
    Solution().solve(board)
    assert expected == board


def test_example_2():
    board = [["X"]]
    expected = [["X"]]
    Solution().solve(board)
    assert expected == board


def test_example_3():
    board = [["O"]]
    expected = [["O"]]
    Solution().solve(board)
    assert expected == board
