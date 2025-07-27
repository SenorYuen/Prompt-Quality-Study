class TicTacToe:
    """
    The class represents a game of Tic-Tac-Toe and its functions include making a move on the board, checking for a winner, and determining if the board is full.
    """

    def __init__(self, N=3):
        """
        Initialize a 3x3 game board with all empty spaces and current symbol player, default is 'X'.
        """
        # Create a 3x3 game board with all empty spaces
        self.board = [[' ' for _ in range(N)] for _ in range(3)]
        # Set the current player to 'X'
        self.current_player = 'X'

    def make_move(self, row, col):
        """
        Place the current player's mark at the specified position on the board and switch the mark.
        :param row: int, the row index of the position
        :param col: int, the column index of the position
        :return: bool, indicating whether the move was successful or not
        """
        # Check if the position is empty
        if self.board[row][col] == ' ':
            # Place the current player's mark at the specified position
            self.board[row][col] = self.current_player
            # Switch the current player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            # Return True to indicate a successful move
            return True
        # Return False to indicate an unsuccessful move
        return False

    def check_winner(self):
        """
        Check if there is a winner on the board in rows, columns and diagonals three directions
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner yet
        """
        # Check rows for a winner
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        # Check columns for a winner
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        # Check diagonals for a winner
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        # Return None if no winner is found
        return None

    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        """
        # Check if any position on the board is empty
        for row in self.board:
            if ' ' in row:
                # Return False if the board is not full
                return False
        # Return True if the board is full
        return True