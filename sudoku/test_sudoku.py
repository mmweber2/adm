from sudoku import Board
from nose.tools import assert_raises
from nose.tools import assert_equals

# Test Board

# Taken from puzzle generator online
def test_board_valid():
    input_array = [[None] * 9 for _ in xrange(9)]
    # In format: (row, column, number)
    positions = (
                (0, 4, 9), (0, 7, 5), (0, 8, 2), (1, 1, 1), (1, 6, 3),
                (1, 8, 4), (2, 2, 2), (2, 3, 3), (2, 4, 1), (2, 5, 5),
                (2, 8, 9), (3, 2, 8), (3, 3, 7), (3, 4, 4), (3, 5, 6),
                (3, 7, 3), (4, 1, 7), (4, 3, 9), (4, 5, 1), (4, 7, 2),
                (5, 1, 9), (5, 3, 2), (5, 4, 5), (5, 5, 3), (5, 6, 7),
                (6, 0, 4), (6, 3, 5), (6, 4, 3), (6, 5, 8), (6, 6, 2),
                (7, 0, 2), (7, 2, 3), (7, 7, 6), (8, 0, 1), (8, 1, 5),
                (8, 4, 6)
            )
    for pos in positions:
        x, y, z = pos
        input_array[x][y] = z
    result = Board._is_valid_start_board(input_array)
    assert result[0]
    assert_equals(result[1], "")

# TODO: Test board with no numbers in it
# TODO: Test board with invalid configuration
