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
        _is_valid_start_board(Board, board_array)
        self.board = board_array

    @staticmethod
    def _is_valid_start_board(board_array):
        """Confirms that board_array is in valid Sudoku format.

        Does not confirm whether it is possible to solve this board.

        Args:
            board_array: The 2D list to check.

        Raises:
            ValueError: board_array is not a valid board configuration.

        Returns:
            True if the board is of the valid format.
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
                      "board_array numbers must be in range 0 <= x <= 9"
                                  )
        # TODO: Call function that says whether board has duplicates
        return True
