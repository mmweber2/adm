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
            Must be in the range 0 <= x < board size, so 0 <= x < 9
            for a standard 9x9 board.

        Returns:
            A set of the non-zero numbers found in this row.

        Raises:
            ValueError: row is outside the valid range for this board.
        """
        if type(row) != int or not (0 <= row < len(self.board_array)):
            raise ValueError("Invalid row number: {}".format(row))
        return set([x for x in board.array[row] if x != 0])

    def _numbers_in_column(self, col):
        """Returns a set of the numbers in this column.

        Zeroes are ignored, since they represent blank spaces.

        Args:
            col: The integer index of the column of this board to check.
            Must be in the range 0 <= x < board size, so 0 <= x < 9
            for a standard 9x9 board.

        Returns:
            A set of the non-zero numbers found in this column.

        Raises:
            ValueError: col is outside the valid range for this board.
        """
        if type(col) != int or not (0 <= col < len(self.board_array)):
            raise ValueError("Invalid column number: {}".format(col))
        board_size = len(self.board_array)
        col_numbers = set()
        for i in xrange(board_size):
            if board_array[i][col] != 0:
                col_numbers.add(board_array[i][col])
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
        for param in (grid_start_row, grid_start_col):
            if type(param) != int or param not in (0, 3, 6):
                raise ValueError("Invalid grid start number: {}".format(param))
        grid_numbers = set()
        # +3 to check 3 numbers from each starting point
        for i in xrange(grid_start_row, grid_start_row + 3):
            for j in xrange(grid_start_col, grid_start_col + 3):
                if self.board_array[i][j] != 0:
                    grid_numbers.add(board_array[i][j])
        return grid_numbers


class Engine(object):
    pass
