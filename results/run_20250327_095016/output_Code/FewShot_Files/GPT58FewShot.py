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
        """
        Generates a minesweeper map with the given size of the board and the number of mines.
        :return: The minesweeper map, list.
        """
        # Initialize the board with zeros
        board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        
        # Place mines randomly
        mines = 0
        while mines < self.k:
            x, y = random.randint(0, self.n - 1), random.randint(0, self.n - 1)
            if board[x][y] != 'X':
                board[x][y] = 'X'
                mines += 1
                
                # Increment numbers around the mine
                for i in range(max(0, x-1), min(self.n, x+2)):
                    for j in range(max(0, y-1), min(self.n, y+2)):
                        if board[i][j] != 'X':
                            board[i][j] += 1
        return board

    def generate_playerMap(self):
        """
        Generates a player map with the given size of the board.
        :return: The player map, list.
        """
        # Initialize the player map with '-' for unknown positions
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self, map):
        """
        Checks whether the player has won the game.
        :return: True if the player has won the game, False otherwise.
        """
        # Check if all non-mine positions are revealed
        for i in range(self.n):
            for j in range(self.n):
                if map[i][j] == '-' and self.minesweeper_map[i][j] != 'X':
                    return False
        return True

    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False otherwise, or the player map if the game continues.
        """
        # Check if the position is a mine
        if self.minesweeper_map[x][y] == 'X':
            self.player_map[x][y] = 'X'
            return False  # Player loses if a mine is swept
        
        # Reveal the position
        self.player_map[x][y] = self.minesweeper_map[x][y]
        
        # Check for win condition
        if self.check_won(self.player_map):
            return True
        
        return self.player_map