class MinesweeperGame:
    def __init__(self, n, k) -> None:
        """
        Initializes the MinesweeperGame class with the size of the board and the number of mines.
        """
        self.n = n  # Size of the board (n x n)
        self.k = k  # Number of mines
        self.mine_map = self.generate_mine_sweeper_map()  # Generate the mine map
        self.player_map = self.generate_playerMap()  # Generate the player map
        self.revealed_cells = 0  # Track the number of revealed cells

    def generate_mine_sweeper_map(self):
        """
        Generates a minesweeper map with the given size of the board and the number of mines.
        'X' represents the mine, other numbers represent the number of mines around the position.
        :return: The minesweeper map, list.
        """
        # Initialize the mine map with zeros
        mine_map = [[0 for _ in range(self.n)] for _ in range(self.n)]

        # Place mines randomly
        mines_placed = 0
        while mines_placed < self.k:
            x, y = random.randint(0, self.n - 1), random.randint(0, self.n - 1)
            if mine_map[x][y] != 'X':
                mine_map[x][y] = 'X'
                mines_placed += 1

                # Increment the count for adjacent cells
                for i in range(max(0, x - 1), min(self.n, x + 2)):
                    for j in range(max(0, y - 1), min(self.n, y + 2)):
                        if mine_map[i][j] != 'X':
                            mine_map[i][j] += 1

        return mine_map

    def generate_playerMap(self):
        """
        Generates a player map with the given size of the board.
        '-' represents the unknown position.
        :return: The player map, list.
        """
        return [['-' for _ in range(self.n)] for _ in range(self.n)]

    def check_won(self):
        """
        Checks whether the player has won the game.
        :return: True if the player has won the game, False otherwise.
        """
        # The player wins if all non-mine cells are revealed
        return self.revealed_cells == self.n * self.n - self.k

    def sweep(self, x, y):
        """
        Sweeps the given position.
        :return: True if the player has won the game, False otherwise, if the game still continues, return the player map, list.
        """
        if self.mine_map[x][y] == 'X':
            return False  # Game over, player hit a mine

        # Use a queue for BFS to reveal connected zero cells
        queue = [(x, y)]
        visited = set()

        while queue:
            cx, cy = queue.pop(0)
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))

            # Reveal the cell
            self.player_map[cx][cy] = self.mine_map[cx][cy]
            self.revealed_cells += 1

            # If the cell is zero, add its neighbors to the queue
            if self.mine_map[cx][cy] == 0:
                for i in range(max(0, cx - 1), min(self.n, cx + 2)):
                    for j in range(max(0, cy - 1), min(self.n, cy + 2)):
                        if (i, j) not in visited and self.player_map[i][j] == '-':
                            queue.append((i, j))

        # Check if the player has won after this move
        if self.check_won():
            return True

        return self.player_map