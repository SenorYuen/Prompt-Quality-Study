import random

class MinesweeperGame:
    """
    This is a class that implements mine sweeping games including minesweeping and winning judgment.
    """

    def __init__(self, n, k) -> None:
        """
        Initializes the MinesweeperGame class with the size of the board and the number of mines.
        :param n: The size of the board, int.
        :param k: The number of mines, int.
        """
        self.n = n
        self.k = k
        self.minesweeper_map = self.generate_mine_sweeper_map()
        self.player_map = self.generate_playerMap()
        self.score = 0

    def generate_mine_sweeper_map(self):
        # Initialize an empty board
        board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        
        # Randomly place mines on the board
        mines = set()
        while len(mines) < self.k:
            x, y = random.randint(0, self.n-1), random.randint(0, self.n-1)
            if (x, y) not in mines:
                board[x][y] = 'X'
                mines.add((x, y))
        
        # Calculate the number of mines around each cell
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] != 'X':
                    count = 0
                    for x in range(max(0, i-1), min(self.n, i+2)):
                        for y in range(max(0, j-1), min(self.n, j+2)):
                            if board[x][y] == 'X':
                                count += 1
                    board[i][j] = count
        
        return board

    def generate_playerMap(self):
        # Initialize a player map with all cells marked as unknown
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self, map):
        # Check if all non-mine cells have been revealed
        for i in range(self.n):
            for j in range(self.n):
                if self.minesweeper_map[i][j] != 'X' and map[i][j] == '-':
                    return False
        return True

    def sweep(self, x, y):
        # Check if the cell is a mine
        if self.minesweeper_map[x][y] == 'X':
            self.player_map[x][y] = 'X'
            return False
        
        # Reveal the cell
        self.player_map[x][y] = self.minesweeper_map[x][y]
        
        # Recursively reveal adjacent cells if the current cell has no adjacent mines
        if self.minesweeper_map[x][y] == 0:
            for i in range(max(0, x-1), min(self.n, x+2)):
                for j in range(max(0, y-1), min(self.n, y+2)):
                    if self.player_map[i][j] == '-':
                        self.sweep(i, j)
        
        # Check if the game is won
        if self.check_won(self.player_map):
            return True
        
        return self.player_map