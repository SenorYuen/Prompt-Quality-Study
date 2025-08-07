import random

class MinesweeperGame:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.minesweeper_map = self.generate_mine_sweeper_map()
        self.player_map = self.generate_playerMap()
        self.score = 0

    def generate_mine_sweeper_map(self):
        minesweeper_map = [[0 for _ in range(self.n)] for _ in range(self.n)]
        mines = set()
        while len(mines) < self.k:
            x = random.randint(0, self.n - 1)
            y = random.randint(0, self.n - 1)
            mines.add((x, y))
        for x, y in mines:
            minesweeper_map[x][y] = 'X'
            for i in range(max(0, x-1), min(self.n, x+2)):
                for j in range(max(0, y-1), min(self.n, y+2)):
                    if minesweeper_map[i][j] != 'X':
                        minesweeper_map[i][j] += 1
        return minesweeper_map

    def generate_playerMap(self):
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self, map):
        for i in range(self.n):
            for j in range(self.n):
                if map[i][j] == '-' and self.minesweeper_map[i][j] != 'X':
                    return False
        return True

    def sweep(self, x, y):
        if self.minesweeper_map[x][y] == 'X':
            return False
        self.player_map[x][y] = self.minesweeper_map[x][y]
        if self.check_won(self.player_map):
            return True
        return self.player_map