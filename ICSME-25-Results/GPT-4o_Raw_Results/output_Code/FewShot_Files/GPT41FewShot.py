class GomokuGame:
    """
    This class is an implementation of a Gomoku game, supporting for making moves, checking for a winner, and checking if there are five consecutive symbols on the game board.
    """

    def __init__(self, board_size):
        """
        Initializes the game with a given board size.
        It initializes the board with empty spaces and sets the current player symbol as 'X'.
        """
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 'X'

    def make_move(self, row, col):
        """
        Makes a move at the given row and column.
        If the move is valid, it places the current player's symbol on the board
        and changes the current player to the other player (if the current player is 'X', then it becomes 'O' and vice versa).
        :param row: int, the row index of this move
        :param col: int, the column index
        return: True if the move is valid, or False otherwise.
        """
        # Check if the move is within the board and the cell is empty
        if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            # Toggle the current player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        """
        Checks if there is a winner by looking for five in a row in all directions (horizontal, vertical, diagonal).
        return: the symbol of the winning player (either 'X' or 'O') if there is a winner, or None otherwise.
        """
        # Directions: horizontal, vertical, diagonal (down-right), diagonal (up-right)
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] != ' ':
                    for direction in directions:
                        if self._check_five_in_a_row(row, col, direction):
                            return self.board[row][col]
        return None

    def _check_five_in_a_row(self, row, col, direction):
        """
        Checks if there are five consecutive symbols of the same player in a row starting from a given cell in a given direction (horizontal, vertical, diagonal).
        Counts the number of consecutive symbols in that direction starting from the given cell.
        :param row: int, row of the given cell
        :param col: int, column of the given cell
        :param direction: tuple, (int, int), named as (dx, dy). Row and col will plus several dx and dy respectively.
        :return: True if there are five consecutive symbols of the same player, and False otherwise.
        """
        dx, dy = direction
        current_symbol = self.board[row][col]
        count = 0

        # Check in the specified direction
        for _ in range(5):
            if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == current_symbol:
                count += 1
                row += dx
                col += dy
            else:
                break

        return count == 5