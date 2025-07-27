class TicTacToe:
    def __init__(self, N=3):
        self.board = [[' ' for _ in range(N)] for _ in range(N)]
        self.current_player = 'X'

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        lines = self.board + [list(col) for col in zip(*self.board)] + [[self.board[i][i] for i in range(3)], [self.board[i][2-i] for i in range(3)]]
        for line in lines:
            if line.count(line[0]) == 3 and line[0] != ' ':
                return line[0]
        return None

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)