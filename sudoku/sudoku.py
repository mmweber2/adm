class Board(object):
    """Represents a Sudoku board."""

    def __init__(self, board_array):
        """Creates a new Sudoku puzzle board.

        Per the rules of Sudoku, each board consists of 9 squares, each
        of which contains 9 numbers in a 3x3 grid. Each number appears
        exactly once in each 3x3 square, row, and column.

        Args:
            board_array: A 9x9 2D list containing the initial board setup.
            Blank spaces are represented by zeroes, and filled spaces are
            represented by integers 1-9.

        Raises:
            ValueError: board_array is not a valid board configuration.
        """
        Board._is_valid_start_board(board_array)
        self.board = board_array

    def board_size(self):
        """Returns the size of the board.

        Since the board must be a square, it will have this many rows
        and columns. The number of numbers (or spaces) on the board will
        be the square of this number.

        The standard board size is 9, totaling 81 spaces.

        Returns:
           An integer indicating the size of the board in rows
           (and columns).
        """
        return len(self.board)

    @staticmethod
    def _is_valid_start_board(board_array):
        """Confirms that board_array is in valid Sudoku format.

        Does not confirm whether it is possible to solve this board.

        Args:
            board_array: The 2D list to check.

        Returns:
            True if the board is of the valid format.

        Raises:
            ValueError: board_array is not a valid board configuration.
        """
        if not type(board_array) in (list, tuple):
            raise ValueError("board_array must be a 2D list")
        if len(board_array) != 9:
            raise ValueError("board_array must contain 9 grids")
        for sublist in board_array:
            if not type(sublist) in (list, tuple):
                raise ValueError("board_array must contain only lists")
            if len(sublist) != 9:
                raise ValueError("board_array grids must be 9x9")
            for item in sublist:
                if type(item) != int:
                    raise ValueError("board_array must contain only integers")
                if not 0 <= item <= 9:
                    raise ValueError(
                        "board_array numbers must be in range 0 <= x <= 9")
        if not Board._is_valid_board(board_array):
            raise ValueError(
                "board_array rows, columns, and grids must not " +
                "contain non-zero duplicates")
        return True

    @staticmethod
    def _is_valid_board(board_array):
        """Determines whether this Board is valid.

        A Board is considered valid if there are no repeating numbers
        (besides 0, which represents a blank space) in any row, column,
        or 3 x 3 grid of the board.
        The 3 x 3 grids divide the board into ninths such that exactly
        9 fit onto the board. For example, there can be repeating numbers
        in the 3 columns that span indecis 1-3, but not 0-2, because 0-2
        and 3-5 are separate grids.

        Args:
            board_array: The 2D list to check.

        Returns:
            True iff the board is valid, and False otherwise.
        """
        # Can't use board_size() here because the Board is not made yet
        board_size = len(board_array)
        # Check rows
        for i in xrange(board_size):
            row_numbers = [x for x in board_array[i] if x != 0]
            unique_size = len(set(row_numbers))
            if unique_size < len(row_numbers):
                return False
        # Check columns
        for j in xrange(board_size):
            col_numbers = set()
            for i in xrange(board_size):
                if board_array[i][j] == 0: continue
                if board_array[i][j] in col_numbers:
                    return False
                col_numbers.add(board_array[i][j])
        # Check grids
        # Start at upper left of each grid, then move 2 in each direction
        grids = (
                (0, 0), (0, 3), (0, 6),
                (3, 0), (3, 3), (3, 6),
                (6, 0), (6, 3), (6, 6))
        for grid in grids:
            grid_numbers = set()
            # +3 to check 3 numbers from each starting point
            for i in xrange(grid[0], grid[0] + 3):
                for j in xrange(grid[1], grid[1] + 3):
                    if board_array[i][j] == 0: continue
                    if board_array[i][j] in grid_numbers:
                        return False
                    grid_numbers.add(board_array[i][j])
        return True

    def _numbers_in_row(self, row):
        """Returns a set of the numbers in this row.

        Zeroes are ignored, since they represent blank spaces.

        Args:
            row: The integer index of the row of this board to check.
            Must be in the range 0 <= x < board_size(), so 0 <= x < 9
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
            Must be in the range 0 <= x < board_size(), so 0 <= x < 9
            for a standard 9x9 board.

        Returns:
            A set of the non-zero numbers found in this column.

        Raises:
            ValueError: col is outside the valid range for this board.
        """
        self._valid_pos(col)
        col_numbers = set()
        for i in xrange(self.board_size()):
            if self.board[i][col] != 0:
                col_numbers.add(self.board[i][col])
        return col_numbers

    def _numbers_in_grid(self, grid_start_row, grid_start_col):
        """Returns a set of the numbers in the given grid.

        Zeroes are ignored, since they represent blank spaces.

        For example, to check the first grid, grid_start_row and
        grid_start_col should be 0 and 0. To check the center grid,
        they should be 3 and 3.

        For a standard 9x9 board, the only acceptable values for grid_start_row
        and grid_start_col are 0, 3, and 6.

        Args:
            grid_start_row: The row index of the upper left most number in the
              grid.

            grid_start_col: The column index of the upper left most number in
              the grid.

        Returns:
            A set of the non-zero numbers found in this grid.

        Raises:
            ValueError: col is outside the valid range for this board.
        """
        # Don't use _valid_pos because grid requirements are more specific
        for param in (grid_start_row, grid_start_col):
            if type(param) != int or param not in (0, 3, 6):
                raise ValueError("Invalid grid start number: {}".format(param))
        grid_numbers = set()
        # +3 to check 3 numbers from each starting point
        for i in xrange(grid_start_row, grid_start_row + 3):
            for j in xrange(grid_start_col, grid_start_col + 3):
                if self.board[i][j] != 0:
                    grid_numbers.add(self.board[i][j])
        return grid_numbers

    def valid_moves(self, row, column):
        """Returns the valid moves for the given position.

        Args:
            row, column: The zero-indexed integer row and column
            numbers for the position to check. Must be in the range
            0 <= x < board_size().

        Returns:
            A list of numbers in the range 1-9 that are not already
            part of the given position's row, column, or grid, and so
            can be played at the given position.

        Raises:
            ValueError: row or column are not integers, or are not in
            the range 0 <= x < board_size.

            IndexError: The position at row, column is not empty; it
            contains a number > 0.
        """
        self._valid_pos(row)
        self._valid_pos(column)
        # Already having a number here would confuse the row, column,
        # and grid checking.
        if self.board[row][column] != 0:
            raise IndexError(
                "Number already at position {},{}: {}".format(
                    row, column, self.board[row][column])
                )
        used_numbers = self._numbers_in_row(row)
        # Combine all the used numbers together because we don't care where
        # they were used, just that they are no longer possible
        used_numbers.update(self._numbers_in_column(column))
        # Round row and column numbers down to grid start positions
        x = row / 3 * 3
        y = column / 3 * 3
        used_numbers.update(self._numbers_in_grid(x, y))
        remaining_moves = []
        for move in xrange(1, 9):
            if move not in used_numbers:
                remaining_moves.append(move)
        return remaining_moves

    def _valid_pos(self, index):
        """Checks whether the given index is valid for this Board.
        
        Args:
            index: The index to check. A valid index is an integer in
            the range 0 <= x < board_size().
            Since all Boards must be square, a valid row is necessarily a
            valid column, and vice versa.
            
        Returns:
            True iff index is a valid row or column index.

        Raises:
            ValueError: index is not an error, or is outside the range
            of this Board.
        """
        if type(index) != int or not (0 <= index < self.board_size()):
            raise ValueError("Position out of range: {}".format(index))
        return True

    # TODO: Move function that:
    # Scans through all the empty positions, tracking their remaining move count
    # If it finds one with 1 move, makes it and restarts
    # If it finds one with 2+ moves, try making each of them and recurse
    # If it finds one with 0 moves, backs up
    # The 2+ move function can hold onto one 2+ move and try it after ensuring
    # that there are no 1 move positions currently on the board
    def make_moves(self):
        """Traverses the Board, making moves where possible.

        Returns:
            True if the Board is completely filled with valid positions,
            or False if the Board is in a dead-end (non-winnable) position.
        """
        # Moves we'd like to explore if there are no 0 or 1 move positions
        potential_moves = []
        # No square can have more than 9 possible moves in it
        move_min = 10
        for i in xrange(self.board_size()):
            for j in xrange(self.board_size()):
                # Skip filled positions
                if self.board[i][j] != 0:
                    continue
                remaining = self.valid_moves(i, j)
                if len(remaining) == 0:
                    return False
                if len(remaining) == 1:
                    self.board[i][j] = remaining[0]
                    # TODO: Find a better way to break out of the loop and restart
                    self.make_moves()
                else:
                    if len(remaining) < move_min:
                        move_min = len(remaining)
                        potential_moves = [[i, j, x for x in remaining]]
                    elif len(remaining) == move_min
                        potential_moves.extend([i, j, x for x in remaining])
        # Check for won position
        if len(potential_moves) == 0:
            return True
        for move in potential_moves:
            i, j, x = move
            self.board[i][j] = x
            # Undo moves that don't work and try more
            if not self.make_moves():
                self.board[i][j] = 0
                self.make_moves()
            # Pass up a True if we found a winning position
            else: return True
