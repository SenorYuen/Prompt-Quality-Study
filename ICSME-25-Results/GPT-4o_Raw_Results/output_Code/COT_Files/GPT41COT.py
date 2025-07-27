class GomokuGame:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 'X'

    def make_move(self, row, col):
        if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] != ' ':
                    if (self._check_five_in_a_row(row, col, (0, 1)) or
                        self._check_five_in_a_row(row, col, (1, 0)) or
                        self._check_five_in_a_row(row, col, (1, 1)) or
                        self._check_five_in_a_row(row, col, (1, -1))):
                        return self.board[row][col]
        return None

    def _check_five_in_a_row(self, row, col, direction):
        dx, dy = direction
        count = 0
        current_symbol = self.board[row][col]
        for _ in range(5):
            if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == current_symbol:
                count += 1
                row += dx
                col += dy
            else:
                break
        return count == 5