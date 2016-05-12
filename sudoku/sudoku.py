from math import sqrt

class Board(object):
    """Represents a Sudoku board."""

    def __init__(self, board_array):
        """Creates a new Sudoku puzzle board.

        Per the rules of Sudoku, each board consists of 9 squares, each
        of which contains 9 numbers in a 3x3 box. Each number appears
        exactly once in each 3x3 square, row, and column.

        Args:
            board_array: A 9x9 2D list containing the initial board setup.
            Blank spaces are represented by zeroes, and filled spaces are
            represented by integers 1-9.

        Raises:
            ValueError: board_array is not a valid board configuration.
        """
        self.board = board_array
        self.board_size = len(board_array)
        self.box_size = int(sqrt(self.board_size))
        self._is_valid_start_board()

    def _is_valid_start_board(self):
        """Confirms that a Board is in valid Sudoku format.

        Does not confirm whether it is possible to solve this board.

        Returns:
            True if the board is of the valid format.

        Raises:
            ValueError: Board is not a valid board configuration.
        """
        if not type(self.board) in (list, tuple):
            raise ValueError("Board must be a 2D list or tuple")
        # box_size converts to an int, so make sure it's really a square number
        if not self.box_size == sqrt(len(self.board)):
            raise ValueError("Board boxes must be square")
        for sublist in self.board:
            if not type(sublist) in (list, tuple):
                raise ValueError("Board must contain only lists or tuples")
            if len(sublist) != len(self.board):
                raise ValueError("Board boxes must be square")
            for item in sublist:
                if type(item) != int:
                    raise ValueError("Board must contain only integers")
                if not 0 <= item <= len(self.board):
                    raise ValueError(
                        "Board numbers must be in range 0 <= x <= board size")
        if not self._is_valid_board():
            raise ValueError(
                "Board rows, columns, and boxes must not " +
                "contain non-zero duplicates")
        return True

    def _is_valid_board(self):
        """Determines whether this Board is valid.

        A Board is considered valid if there are no repeating numbers
        (besides 0, which represents a blank space) in any row, column,
        or box of the board. Boxes must be square, and are 3 x 3 on
        a standard board.
        For a standard board, the 3 x 3 boxes divide the board into ninths
        such that exactly 9 fit onto the board. For example, there can be
        repeating numbers in the 3 columns that span indices 1-3, but not
        0-2, because 0-2 and 3-5 are separate boxes.

        Returns:
            True iff the board is valid, and False otherwise.
        """
        # Check rows
        for i in xrange(self.board_size):
            row_numbers = set()
            for number in self.board[i]:
                if number != 0 and number in row_numbers:
                    return False
                # 0s will get added to col_numbers, but that's ok
                row_numbers.add(number)
        # Check columns
        for j in xrange(self.board_size):
            col_numbers = set()
            for i in xrange(self.board_size):
                number = self.board[i][j]
                if number != 0 and number in col_numbers:
                    return False
                col_numbers.add(number)
        # Check boxes
        # Start at upper left of each box, then move one box width in each direction
        move_range = xrange(0, self.board_size, self.box_size)
        boxes = [(x, y) for x in move_range for y in move_range]
        for box in boxes:
            box_numbers = set()
            for i in xrange(box[0], box[0] + self.box_size):
                for j in xrange(box[1], box[1] + self.box_size):
                    number = self.board[i][j]
                    if number != 0 and number in box_numbers:
                        return False
                    box_numbers.add(number)
        return True

    def _numbers_in_row(self, row):
        """Returns a set of the numbers in this row.

        Zeroes are ignored, since they represent blank spaces.

        Args:
            row: The integer index of the row of this board to check.
            Must be in the range 0 <= x < board_size, so 0 <= x < 9
            for a standard 9x9 board.

        Returns:
            A set of the non-zero numbers found in this row.

        Raises:
            ValueError: row is outside the valid range for this board.
        """
        self._valid_pos(row)
        return set([x for x in self.board[row] if x != 0])

    def _numbers_in_column(self, col):
        """Returns a set of the numbers in this column.

        Zeroes are ignored, since they represent blank spaces.

        Args:
            col: The integer index of the column of this board to check.
            Must be in the range 0 <= x < board_size, so 0 <= x < 9
            for a standard 9x9 board.

        Returns:
            A set of the non-zero numbers found in this column.

        Raises:
            ValueError: col is outside the valid range for this board.
        """
        self._valid_pos(col)
        col_numbers = set()
        for i in xrange(self.board_size):
            if self.board[i][col] != 0:
                col_numbers.add(self.board[i][col])
        return col_numbers

    def _numbers_in_box(self, box_start_row, box_start_col):
        """Returns a set of the numbers in the given box.

        Zeroes are ignored, since they represent blank spaces.

        For example, to check the first box, box_start_row and
        box_start_col should be 0 and 0. To check the center box,
        they should be 3 and 3.

        For a standard 9x9 board, the only acceptable values for box_start_row
        and box_start_col are 0, 3, and 6.

        Args:
            box_start_row: The row index of the upper left most number in the
              box.

            box_start_col: The column index of the upper left most number in
              the box.

        Returns:
            A set of the non-zero numbers found in this box.

        Raises:
            ValueError: col is outside the valid range for this board.
        """
        # Don't use _valid_pos because box requirements are more specific
        size = self.board_size
        for p in (box_start_row, box_start_col):
            if type(p) != int or not (0 <= p < size and p % self.box_size == 0):
                raise ValueError("Invalid box start number: {}".format(p))
        box_numbers = set()
        for i in xrange(box_start_row, box_start_row + self.box_size):
            for j in xrange(box_start_col, box_start_col + self.box_size):
                if self.board[i][j] != 0:
                    box_numbers.add(self.board[i][j])
        return box_numbers

    def valid_moves(self, row, column):
        """Returns the valid moves for the given position.

        Args:
            row, column: The zero-indexed integer row and column
            numbers for the position to check. Must be in the range
            0 <= x < board_size.

        Returns:
            A list of numbers in the range 1 to board size that are not
            already part of the given position's row, column, or box, and so
            can be played at the given position.

        Raises:
            ValueError: row or column are not integers, or are not in
            the range 0 <= x < board size.

            IndexError: The position at row, column is not empty; it
            contains a number > 0.
        """
        self._valid_pos(row)
        self._valid_pos(column)
        if self.board[row][column] != 0:
            raise IndexError(
                "Non-zero Number already at position {},{}: {}".format(
                    row, column, self.board[row][column])
                )
        used_numbers = self._numbers_in_row(row)
        # Combine all the used numbers together because we don't care where
        # they were used, just that they are no longer possible
        used_numbers.update(self._numbers_in_column(column))
        # Round row and column numbers down to box start positions
        x = row / self.box_size * self.box_size
        y = column / self.box_size * self.box_size
        used_numbers.update(self._numbers_in_box(x, y))
        return [move for move in xrange(1, 10) if move not in used_numbers]

    def _valid_pos(self, index):
        """Checks whether the given index is valid for this Board.
        
        Args:
            index: The index to check. A valid index is an integer in
            the range 0 <= x < board_size.
            Since all Boards must be square, a valid row is necessarily a
            valid column, and vice versa.
            
        Returns:
            True iff index is a valid row or column index.

        Raises:
            ValueError: index is not an error, or is outside the range
            of this Board.
        """
        if type(index) != int or not 0 <= index < self.board_size:
            raise ValueError("Position out of range: {}".format(index))
        return True

    def make_moves(self):
        """Traverses the Board, making moves where possible.

        Returns:
            A complete board solution (as a 2D list) if the Board is
            completely filled with valid positions, or None if the
            Board is in a dead-end (non-winnable) position.
        """
        # Moves we'd like to explore if there are no 0 or 1 move positions
        next_move = None
        smallest_move = self.board_size + 1
        for i in xrange(self.board_size):
            for j in xrange(self.board_size):
                # Skip filled positions
                if self.board[i][j] != 0:
                    continue
                remaining = self.valid_moves(i, j)
                # Dead-end position, so end this recursion
                if len(remaining) == 0:
                    return None
                if len(remaining) == 1:
                    # Make move and recurse
                    self.board[i][j] = remaining[0]
                    result = self.make_moves()
                    if result == None:
                        self.board[i][j] = 0
                        return None
                    return result
                else:
                    # Find most constrained position, if no 1s or 0s
                    if len(remaining) < smallest_move:
                        smallest_move = len(remaining)
                        next_move = (i, j, remaining)
        # Check for won position
        if next_move == None:
            if self._is_valid_board():
                return self.board
        i, j = next_move[0], next_move[1]
        for move in next_move[2]:
            self.board[i][j] = move
            board_result = self.make_moves()
            if board_result == None:
                self.board[i][j] = 0
            # Pass up the board if we found a winning position
            else: return board_result
        return None
