from sudoku import Board
from nose.tools import assert_raises
from nose.tools import assert_equals

# Test Board

# Taken from puzzle generator online
def test_is_valid_start_board_valid():
    input_array = [
                   [0, 0, 0, 0, 9, 0, 0, 5, 2],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    assert Board._is_valid_start_board(input_array)

def test_board_constructor_valid():
    input_array = [
                   [0, 0, 0, 0, 9, 0, 0, 5, 2],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    b = Board(input_array)
    assert_equals(b.board, input_array)

def test_is_valid_start_board_wrong_outer_size():
    input_array = [[1, 0], [0, 0]]
    with assert_raises(ValueError) as cm:
      Board._is_valid_start_board(input_array)
    assert_equals(str(cm.exception), "board_array must contain 9 grids")

def test_board_constructor_invalid():
    input_array = [[1, 0], [0, 0]]
    b = None
    with assert_raises(ValueError) as cm:
      Board(input_array)
    assert_equals(str(cm.exception), "board_array must contain 9 grids")
    assert_equals(b, None)

def test_is_valid_start_board_wrong_inner_size():
    input_array = [[1, 0], [0, 0], [0, 0],
                   [0, 0], [0, 0], [0, 0],
                   [0, 0], [0, 0], [0, 0]
                  ]
    with assert_raises(ValueError) as cm:
      Board._is_valid_start_board(input_array)
    assert_equals(str(cm.exception), "board_array grids must be 9x9")

def test_is_valid_start_board_not_list():
    input_array = "abcd"
    with assert_raises(ValueError) as cm:
      Board._is_valid_start_board(input_array)
    assert_equals(str(cm.exception), "board_array must be a 2D list")

def test_is_valid_start_board_no_inner_list():
    input_array = ["abcd", "efgh", "i", "j", "k", "l", "m", "n", "o"]
    with assert_raises(ValueError) as cm:
      Board._is_valid_start_board(input_array)
    assert_equals(str(cm.exception), "board_array must contain only lists")

# For now, an empty board is valid
def test_is_valid_start_board_empty():
    assert Board._is_valid_start_board([[0] * 9 for _ in xrange(9)])

def test_is_valid_start_board_non_int():
    input_array = [[0] * 9 for _ in xrange(9)]
    input_array[2][2] = "abc"
    with assert_raises(ValueError) as cm:
      Board._is_valid_start_board(input_array)
    assert_equals(str(cm.exception), "board_array must contain only integers")

def test_is_valid_start_board_invalid_ints():
    input_array = [[0] * 9 for _ in xrange(9)]
    input_array[2][2] = 10
    with assert_raises(ValueError) as cm:
      Board._is_valid_start_board(input_array)
    assert_equals(
        str(cm.exception), "board_array numbers must be in range 0 <= x <= 9"
                 )

def test_is_valid_start_board_duplicates():
    input_array = [
                   # 2 2s in this row
                   [0, 0, 0, 0, 9, 2, 0, 5, 2],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    assert_raises(ValueError, Board._is_valid_start_board, input_array)

def test_is_valid_board_valid():
    input_array = [
                   [0, 0, 0, 0, 9, 0, 0, 5, 2],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    assert Board._is_valid_board(input_array)

# Duplicates are somewhat hidden in the grids because I wanted to test
# situations where only the row, column, or grid had a duplicate, and
# not multiple situations at the same time.
def test_is_valid_board_duplicate_row():
    input_array = [
                   # 2 2s in this row
                   [0, 0, 0, 0, 9, 2, 0, 5, 2],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    assert not Board._is_valid_board(input_array)

def test_is_valid_board_duplicate_column():
    input_array = [
                   [0, 0, 0, 0, 9, 0, 0, 5, 2],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [1, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [1, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   # second 1 in the first column
                   [0, 5, 0, 0, 6, 1, 0, 0, 0]
                  ]
    assert not Board._is_valid_board(input_array)

def test_is_valid_board_duplicate_in_grid():
    input_array = [
                   # second grid in first row has two 1s
                   [0, 0, 0, 1, 9, 0, 0, 5, 2],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    assert not Board._is_valid_board(input_array)

# The _numbers_in_row tests don't need checking for duplicates because
# that will be done when the board is created.
def test_numbers_in_row_valid():
    input_array = [
                   [0, 0, 0, 0, 9, 0, 0, 5, 2],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    b = Board(input_array)
    result = b._numbers_in_row(0)
    # Two sets are equal iff every element of each set is contained in the other
    assert_equals(result, set((2, 5, 9)))

def test_numbers_in_row_empty():
    input_array = [
                   # Clear out non-zeroes in first row
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    b = Board(input_array)
    assert_equals(b._numbers_in_row(0), set())

def test_numbers_in_row_invalid_row():
    input_array = [
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    b = Board(input_array)
    assert_raises(ValueError, b._numbers_in_row, 9)

def test_numbers_in_col_valid():
    input_array = [
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    b = Board(input_array)
    assert_equals(b._numbers_in_column(8), set((4, 9)))

def test_numbers_in_col_invalid_col():
    input_array = [
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [0, 0, 0, 5, 3, 8, 2, 0, 0],
                   [0, 0, 3, 0, 0, 0, 0, 6, 0],
                   [0, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    b = Board(input_array)
    assert_raises(ValueError, b._numbers_in_column, "4")

def test_numbers_in_grid_valid():
    input_array = [
                   [0, 0, 0, 0, 9, 0, 0, 5, 2],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    b = Board(input_array)
    assert_equals(b._numbers_in_grid(3, 3), set((7, 4, 6, 9, 1, 2, 5, 3)))

def test_numbers_in_grid_invalid_params():
    input_array = [
                   [0, 0, 0, 0, 9, 0, 0, 5, 2],
                   [0, 1, 0, 0, 0, 0, 3, 0, 4],
                   [0, 0, 2, 3, 1, 5, 0, 0, 9],
                   [0, 0, 8, 7, 4, 6, 0, 3, 0],
                   [0, 7, 0, 9, 0, 1, 0, 2, 0],
                   [0, 9, 0, 2, 5, 3, 7, 0, 0],
                   [4, 0, 0, 5, 3, 8, 2, 0, 0],
                   [2, 0, 3, 0, 0, 0, 0, 6, 0],
                   [1, 5, 0, 0, 6, 0, 0, 0, 0]
                  ]
    b = Board(input_array)
    assert_raises(ValueError, b._numbers_in_grid, 1, 1)
