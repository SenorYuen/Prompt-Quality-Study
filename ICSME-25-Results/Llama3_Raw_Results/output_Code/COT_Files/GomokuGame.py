class GomokuGame:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 'X'

    def make_move(self, row, col):
        if self.board[row][col] != ' ':
            return False
        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True

    def check_winner(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] != ' ':
                    for direction in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                        if self._check_five_in_a_row(row, col, direction):
                            return self.board[row][col]
        return None

    def _check_five_in_a_row(self, row, col, direction):
        symbol = self.board[row][col]
        count = 1
        for i in range(1, 5):
            new_row, new_col = row + i * direction[0], col + i * direction[1]
            if (0 <= new_row < self.board_size and 0 <= new_col < self.board_size and
                    self.board[new_row][new_col] == symbol):
                count += 1
            else:
                break
        for i in range(1, 5):
            new_row, new_col = row - i * direction[0], col - i * direction[1]
            if (0 <= new_row < self.board_size and 0 <= new_col < self.board_size and
                    self.board[new_row][new_col] == symbol):
                count += 1
            else:
                break
        return count >= 5