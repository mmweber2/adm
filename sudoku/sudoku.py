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
            row_numbers = set()
            for j in xrange(board_size):
                if board_array[i][j] == 0: continue
                if board_array[i][j] in row_numbers:
                    return False
                row_numbers.add(board_array[i][j])
        # Check columns
        for j in xrange(board_size):
            col_numbers = set()
            for i in xrange(board_size):
                if board_array[i][j] == 0: continue
                if board_array[i][j] in col_numbers:
                    return False
                col_numbers.add(board_array[i][j])
        # Check grids
        grids = ((0, 2), (3, 5), (6, 8))
        for grid in grids:
            grid_numbers = set()
            for i in xrange(*grid):
                for j in xrange(*grid):
                    if board_array[i][j] == 0: continue
                    if board_array[i][j] in grid_numbers:
                        return False
                    grid_numbers.add(board_array[i][j])
        return True


