import random

class MinesweeperGame:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.minesweeper_map = self.generate_mine_sweeper_map()
        self.player_map = self.generate_playerMap()
        self.score = 0

    def generate_mine_sweeper_map(self):
        # Initialize the board
        board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        
        # Place mines randomly
        mine_positions = random.sample(range(self.n * self.n), self.k)
        for pos in mine_positions:
            x, y = divmod(pos, self.n)
            board[x][y] = 'X'
        
        # Calculate numbers for non-mine cells
        for x in range(self.n):
            for y in range(self.n):
                if board[x][y] == 'X':
                    continue
                # Count surrounding mines
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < self.n and 0 <= ny < self.n and board[nx][ny] == 'X':
                            count += 1
                board[x][y] = count
        return board

    def generate_playerMap(self):
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self, map):
        for x in range(self.n):
            for y in range(self.n):
                if map[x][y] == '-' and self.minesweeper_map[x][y] != 'X':
                    return False
        return True

    def sweep(self, x, y):
        if self.minesweeper_map[x][y] == 'X':
            self.player_map[x][y] = 'X'
            return False
        else:
            self.player_map[x][y] = self.minesweeper_map[x][y]
            if self.check_won(self.player_map):
                return True
            return self.player_map