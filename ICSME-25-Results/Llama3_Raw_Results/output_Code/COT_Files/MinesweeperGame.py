import random

class MinesweeperGame:
    def __init__(self, n, k):
        """
        Initializes the MinesweeperGame class with the size of the board and the number of mines.
        
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
        Generates a minesweeper map with the given size of the board and the number of mines.
        
        Returns:
            list: The minesweeper map as a 2D list.
        """
        # Initialize an empty map with all zeros
        map = [[0 for _ in range(self.n)] for _ in range(self.n)]
        
        # Randomly place the mines
        mines_placed = 0
        while mines_placed < self.k:
            x, y = random.randint(0, self.n-1), random.randint(0, self.n-1)
            if map[x][y] != 'X':
                map[x][y] = 'X'
                mines_placed += 1
        
        # Update the map with the number of mines around each position
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
        Generates a player map with the given size of the board.
        
        Returns:
            list: The player map as a 2D list.
        """
        # Initialize an empty map with all unknown positions
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self, map):
        """
        Checks whether the player has won the game.
        
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
        Sweeps the given position.
        
        Args:
            x (int): The x coordinate of the position.
            y (int): The y coordinate of the position.
        
        Returns:
            list or bool: The updated player map if the game continues, True if the player has won.
        """
        # Check if the position is a mine
        if self.minesweeper_map[x][y] == 'X':
            self.player_map[x][y] = 'X'
            return self.player_map
        else:
            # Reveal the position and recursively reveal adjacent positions
            self.player_map[x][y] = self.minesweeper_map[x][y]
            if self.minesweeper_map[x][y] == 0:
                for i in range(max(0, x-1), min(self.n, x+2)):
                    for j in range(max(0, y-1), min(self.n, y+2)):
                        if self.player_map[i][j] == '-':
                            self.sweep(i, j)
            # Check if the player has won
            if self.check_won(self.player_map):
                return True
            else:
                return self.player_map