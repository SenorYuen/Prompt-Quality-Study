import random

class MinesweeperGame:
    def __init__(self, n, k):
        """
        Initialize the MinesweeperGame class with the size of the board and the number of mines.
        
        Args:
            n (int): The size of the board.
            k (int): The number of mines.
        """
        self.n = n
        self.k = k
        self.minesweeper_map = self.generate_mine_sweeper_map()
        self.player_map = self.generate_playerMap()
        self.score = 0

    def generate_mine_sweeper_map(self):
        """
        Generate a minesweeper map with the given size of the board and the number of mines.
        
        Returns:
            list: The minesweeper map.
        """
        # Initialize the map with zeros
        map = [[0 for _ in range(self.n)] for _ in range(self.n)]
        
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
                    for x in range(max(0, i-1), min(self.n, i+2)):
                        for y in range(max(0, j-1), min(self.n, j+2)):
                            if map[x][y] == 'X':
                                count += 1
                    map[i][j] = count
        
        return map

    def generate_playerMap(self):
        """
        Generate a player map with the given size of the board.
        
        Returns:
            list: The player map.
        """
        # Initialize the map with unknown positions
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self, map):
        """
        Check whether the player has won the game.
        
        Args:
            map (list): The player map.
        
        Returns:
            bool: True if the player has won, False otherwise.
        """
        # Check if all non-mine positions are revealed
        for i in range(self.n):
            for j in range(self.n):
                if self.minesweeper_map[i][j] != 'X' and map[i][j] == '-':
                    return False
        return True

    def sweep(self, x, y):
        """
        Sweep the given position.
        
        Args:
            x (int): The x coordinate of the position.
            y (int): The y coordinate of the position.
        
        Returns:
            bool or list: True if the player has won, False if the game continues, or the updated player map.
        """
        # Check if the position is within the board
        if x < 0 or x >= self.n or y < 0 or y >= self.n:
            return False
        
        # Check if the position is already revealed
        if self.player_map[x][y] != '-':
            return False
        
        # Reveal the position
        self.player_map[x][y] = self.minesweeper_map[x][y]
        
        # Check if the player has won
        if self.check_won(self.player_map):
            return True
        
        # If the revealed position is a mine, end the game
        if self.minesweeper_map[x][y] == 'X':
            return False
        
        # If the revealed position is a zero, recursively reveal all adjacent positions
        if self.minesweeper_map[x][y] == 0:
            for i in range(max(0, x-1), min(self.n, x+2)):
                for j in range(max(0, y-1), min(self.n, y+2)):
                    self.sweep(i, j)
        
        return self.player_map