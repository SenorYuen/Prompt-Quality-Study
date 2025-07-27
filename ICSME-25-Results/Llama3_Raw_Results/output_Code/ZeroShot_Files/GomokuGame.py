class GomokuGame:
    def __init__(self, board_size):
        # Initialize the board with empty spaces
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        # Set the current player symbol as 'X'
        self.current_player = 'X'
        # Store the board size for later use
        self.board_size = board_size

    def make_move(self, row, col):
        # Check if the move is within the board boundaries
        if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
            return False
        # Check if the cell is already occupied
        if self.board[row][col] != ' ':
            return False
        # Place the current player's symbol on the board
        self.board[row][col] = self.current_player
        # Change the current player to the other player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True

    def check_winner(self):
        # Check all cells on the board for a winner
        for row in range(self.board_size):
            for col in range(self.board_size):
                # Check if the cell is occupied by a player
                if self.board[row][col] != ' ':
                    # Check all directions for five consecutive symbols
                    for direction in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                        if self._check_five_in_a_row(row, col, direction):
                            return self.board[row][col]
        # If no winner is found, return None
        return None

    def _check_five_in_a_row(self, row, col, direction):
        # Get the symbol of the player at the given cell
        symbol = self.board[row][col]
        # Initialize a counter for consecutive symbols
        count = 1
        # Check in the positive direction
        r, c = row + direction[0], col + direction[1]
        while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == symbol:
            count += 1
            r += direction[0]
            c += direction[1]
        # Check in the negative direction
        r, c = row - direction[0], col - direction[1]
        while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == symbol:
            count += 1
            r -= direction[0]
            c -= direction[1]
        # Return True if there are five consecutive symbols, False otherwise
        return count >= 5