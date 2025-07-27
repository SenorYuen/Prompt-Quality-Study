class TicTacToe:
    def __init__(self, N=3):
        """
        Initialize a NxN game board with all empty spaces and current symbol player, default is 'X'.
        """
        # Initialize the board with N rows and N columns
        self.board = [[' ' for _ in range(N)] for _ in range(N)]
        self.N = N  # Store the size of the board
        self.current_player = 'X'

    def make_move(self, row, col):
        """
        Place the current player's mark at the specified position on the board and switch the mark.
        :return: bool, indicating whether the move was successful or not
        """
        # Check if the move is within the board boundaries
        if row < 0 or row >= self.N or col < 0 or col >= self.N:
            return False
        # Check if the space is already occupied
        if self.board[row][col] != ' ':
            return False
        # Make the move
        self.board[row][col] = self.current_player
        # Switch the current player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True

    def check_winner(self):
        """
        Check if there is a winner on the board in rows, columns and diagonals three directions
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner yet
        """
        # Check rows
        for row in self.board:
            if len(set(row)) == 1 and row[0] != ' ':
                return row[0]
        # Check columns
        for col in range(self.N):
            check = []
            for row in self.board:
                check.append(row[col])
            if len(set(check)) == 1 and check[0] != ' ':
                return check[0]
        # Check main diagonal
        main_diagonal = [self.board[i][i] for i in range(self.N)]
        if len(set(main_diagonal)) == 1 and main_diagonal[0] != ' ':
            return main_diagonal[0]
        # Check anti-diagonal
        anti_diagonal = [self.board[i][self.N - i - 1] for i in range(self.N)]
        if len(set(anti_diagonal)) == 1 and anti_diagonal[0] != ' ':
            return anti_diagonal[0]
        # If no winner, return None
        return None

    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        """
        # Check if any space is empty
        for row in self.board:
            if ' ' in row:
                return False
        # If no empty space, the board is full
        return True

# Example usage:
if __name__ == "__main__":
    game = TicTacToe()
    print(game.make_move(0, 0))  # True
    print(game.make_move(0, 0))  # False
    print(game.make_move(1, 1))  # True
    print(game.check_winner())  # None
    print(game.is_board_full())  # False