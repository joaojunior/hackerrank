from minesweeper import Solution


def test_example_1():
    board = [["E", "E", "E", "E", "E"],
             ["E", "E", "M", "E", "E"],
             ["E", "E", "E", "E", "E"],
             ["E", "E", "E", "E", "E"]]
    click = [3, 0]
    expected = [["B", "1", "E", "1", "B"],
                ["B", "1", "M", "1", "B"],
                ["B", "1", "1", "1", "B"],
                ["B", "B", "B", "B", "B"]]
    assert expected == Solution().update_board(board, click)


def test_example_2():
    board = [["B", "1", "E", "1", "B"],
             ["B", "1", "M", "1", "B"],
             ["B", "1", "1", "1", "B"],
             ["B", "B", "B", "B", "B"]]
    click = [1, 2]
    expected = [["B", "1", "E", "1", "B"],
                ["B", "1", "X", "1", "B"],
                ["B", "1", "1", "1", "B"],
                ["B", "B", "B", "B", "B"]]
    assert expected == Solution().update_board(board, click)
