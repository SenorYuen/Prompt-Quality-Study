import random

class MahjongConnect:
    def __init__(self, BOARD_SIZE, ICONS):
        # Initialize the board size and the icon list
        self.BOARD_SIZE = BOARD_SIZE
        self.ICONS = ICONS
        # Create the game board
        self.board = self.create_board()

    def create_board(self):
        # Create the game board with the given board size and icons
        board = []
        for _ in range(self.BOARD_SIZE[0]):
            row = []
            for _ in range(self.BOARD_SIZE[1]):
                # Randomly select an icon from the icon list
                row.append(random.choice(self.ICONS))
            board.append(row)
        return board

    def is_valid_move(self, pos1, pos2):
        # Check if the move of two icons is valid
        # Check if positions are within the game board range
        if (pos1[0] < 0 or pos1[0] >= self.BOARD_SIZE[0] or 
            pos1[1] < 0 or pos1[1] >= self.BOARD_SIZE[1] or 
            pos2[0] < 0 or pos2[0] >= self.BOARD_SIZE[0] or 
            pos2[1] < 0 or pos2[1] >= self.BOARD_SIZE[1]):
            return False
        # Check if the two positions are not the same
        if pos1 == pos2:
            return False
        # Check if the two positions have the same icon
        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False
        # Check if there is a valid path between the two positions
        if not self.has_path(pos1, pos2):
            return False
        return True

    def has_path(self, pos1, pos2):
        # Check if there is a path between two icons
        # Define the possible movements (up, down, left, right)
        movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # Perform a depth-first search to find a path
        def dfs(pos, visited):
            if pos == pos2:
                return True
            visited.add(pos)
            for movement in movements:
                new_pos = (pos[0] + movement[0], pos[1] + movement[1])
                if (0 <= new_pos[0] < self.BOARD_SIZE[0] and 
                    0 <= new_pos[1] < self.BOARD_SIZE[1] and 
                    new_pos not in visited and 
                    self.board[new_pos[0]][new_pos[1]] == self.board[pos1[0]][pos1[1]]):
                    if dfs(new_pos, visited):
                        return True
            return False
        return dfs(pos1, set())

    def remove_icons(self, pos1, pos2):
        # Remove the connected icons on the game board
        self.board[pos1[0]][pos1[1]] = ' '
        self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        # Check if the game is over (i.e., if there are no more icons on the game board)
        for row in self.board:
            for icon in row:
                if icon != ' ':
                    return False
        return True