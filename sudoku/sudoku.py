class Board(object):
    """Represents a Sudoku board."""

    def __init__(self, board_array):
        """Creates a new Sudoku puzzle board.

        Per the rules of Sudoku, each board consists of 9 squares, each
        of which contains 9 numbers in a 3x3 grid. Each number appears
        exactly once in each 3x3 square, row, and column.

        Args:
            board_array: A 9x9 2D list containing the initial board setup.
            Blank spaces are represented by None, and filled spaces are
            represented by integers 1-9.

        Raises:
            ValueError: board_array is not a valid board configuration.
        """
        is_valid, error = Board._is_valid_board(board_array):
        if not is_valid:
            raise ValueError(error)
        self.board = board_array

    @staticmethod
    def _is_valid_start_board(cls, board_array):
        """Confirms that board_array is in valid Sudoku format.

        Does not confirm whether it is possible to solve this board.

        Args:
            board_array: The 2D list to check.

        Returns:
            A tuple of the format (is_valid, error_message).
            If the board is of the valid format, error_message will
            be an empty string; otherwise, it will be an error message
            explaining what is invalid about the board.
            If there are multiple problems with the board, only one such
            reason will be given.
        """
        is_valid = True
        error = ""
        if not (type(board_array) == list:
            is_valid = False
            error = "board_array must be a 2D list"
        elif not len(board_array) == 9:
            is_valid = False
            error = "board_array must contain 9 grids"
        else:
            for sublist in board_array:
                if not type(sublist) == list:
                    is_valid = False
                    error = "board_array must contain only lists"
                elif not len(sublist) == 9:
                    is_valid = False
                    error = "board_array grids must be 9x9"
                else:
                    is_int = [True for item in sublist if type(item) == int]
                    if not all(is_int):
                        is_valid = False
                        error = "All elements in board_array must be integers"
        # TODO: Call function that says whether board has duplicates
        return (is_valid, error)
