class GomokuGame:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 'X'

    def make_move(self, row, col):
        if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size or self.board[row][col] != ' ':
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
            if new_row < 0 or new_row >= self.board_size or new_col < 0 or new_col >= self.board_size or self.board[new_row][new_col] != symbol:
                break
            count += 1
        for i in range(1, 5):
            new_row, new_col = row - i * direction[0], col - i * direction[1]
            if new_row < 0 or new_row >= self.board_size or new_col < 0 or new_col >= self.board_size or self.board[new_row][new_col] != symbol:
                break
            count += 1
        return count >= 5