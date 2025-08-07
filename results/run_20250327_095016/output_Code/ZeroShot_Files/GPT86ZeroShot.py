class TicTacToe:
    def __init__(self, N=3):
        """
        Initialize a 3x3 game board with all empty spaces and current player symbol, default is 'X'.
        """
        self.board = [[' ' for _ in range(N)] for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, row, col):
        """
        Place the current player's mark at the specified position on the board and switch the mark.
        :param row: int, the row index for the move
        :param col: int, the column index for the move
        :return: bool, indicating whether the move was successful or not
        """
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            # Switch the current player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        else:
            return False

    def check_winner(self):
        """
        Check if there is a winner on the board in rows, columns, and diagonals.
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

        # No winner found
        return None

    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        """
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True