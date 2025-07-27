import random

class MinesweeperGame:
    def __init__(self, n, k) -> None:
        # Initialize the size of the board and the number of mines
        self.n = n
        self.k = k
        # Initialize the minesweeper map and the player map
        self.minesweeper_map = self.generate_mine_sweeper_map()
        self.player_map = self.generate_playerMap()

    def generate_mine_sweeper_map(self):
        # Create an empty map with the given size
        map = [['0' for _ in range(self.n)] for _ in range(self.n)]
        # Randomly place the mines
        mines = random.sample(range(self.n * self.n), self.k)
        for mine in mines:
            x, y = mine // self.n, mine % self.n
            map[x][y] = 'X'
        # Calculate the number of mines around each position
        for i in range(self.n):
            for j in range(self.n):
                if map[i][j] != 'X':
                    count = 0
                    for x in range(max(0, i - 1), min(self.n, i + 2)):
                        for y in range(max(0, j - 1), min(self.n, j + 2)):
                            if map[x][y] == 'X':
                                count += 1
                    map[i][j] = str(count)
        return map

    def generate_playerMap(self):
        # Create a map with the given size and all positions unknown
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self, map):
        # Check if there are just mines in the player map
        for i in range(self.n):
            for j in range(self.n):
                if map[i][j] != 'X' and map[i][j] == '-':
                    return False
        return True

    def sweep(self, x, y):
        # Check if the position is within the board
        if x < 0 or x >= self.n or y < 0 or y >= self.n:
            return False
        # Check if the position is a mine
        if self.minesweeper_map[x][y] == 'X':
            self.player_map[x][y] = 'X'
            return self.check_won(self.player_map)
        # Reveal the position and recursively reveal adjacent positions
        else:
            self.player_map[x][y] = self.minesweeper_map[x][y]
            if self.minesweeper_map[x][y] == '0':
                for i in range(max(0, x - 1), min(self.n, x + 2)):
                    for j in range(max(0, y - 1), min(self.n, y + 2)):
                        if self.player_map[i][j] == '-':
                            self.sweep(i, j)
            return self.check_won(self.player_map)

# Example usage:
game = MinesweeperGame(10, 10)
print("Minesweeper Map:")
for row in game.minesweeper_map:
    print(row)
print("Player Map:")
for row in game.player_map:
    print(row)
print(game.sweep(5, 5))