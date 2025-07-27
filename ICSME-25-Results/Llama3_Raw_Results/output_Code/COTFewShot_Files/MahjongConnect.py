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
        board = [[random.choice(self.ICONS) for _ in range(self.BOARD_SIZE[1])] for _ in range(self.BOARD_SIZE[0])]
        return board

    def is_valid_move(self, pos1, pos2):
        # Check if the move of two icons is valid
        # Check if positions are within the game board range
        if pos1[0] < 0 or pos1[0] >= self.BOARD_SIZE[0] or pos1[1] < 0 or pos1[1] >= self.BOARD_SIZE[1]:
            return False
        if pos2[0] < 0 or pos2[0] >= self.BOARD_SIZE[0] or pos2[1] < 0 or pos2[1] >= self.BOARD_SIZE[1]:
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
        # Create a queue for BFS and add the starting position
        queue = [(pos1, [pos1])]
        # Create a set to store the visited positions
        visited = set()
        while queue:
            (x, y), path = queue.pop(0)
            # If the current position is the target position, return True
            if (x, y) == pos2:
                return True
            # Mark the current position as visited
            visited.add((x, y))
            # Check all possible movements
            for dx, dy in movements:
                nx, ny = x + dx, y + dy
                # Check if the new position is within the game board range and not visited
                if 0 <= nx < self.BOARD_SIZE[0] and 0 <= ny < self.BOARD_SIZE[1] and (nx, ny) not in visited:
                    # If the new position has the same icon, add it to the queue
                    if self.board[nx][ny] == self.board[pos1[0]][pos1[1]]:
                        queue.append(((nx, ny), path + [(nx, ny)]))
        # If no path is found, return False
        return False

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