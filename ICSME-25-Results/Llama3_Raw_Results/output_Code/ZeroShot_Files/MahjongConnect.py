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
        # Check if the positions are within the game board range
        if (pos1[0] < 0 or pos1[0] >= self.BOARD_SIZE[0] or pos1[1] < 0 or pos1[1] >= self.BOARD_SIZE[1] or
            pos2[0] < 0 or pos2[0] >= self.BOARD_SIZE[0] or pos2[1] < 0 or pos2[1] >= self.BOARD_SIZE[1]):
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
        # Define the possible movements (up, down, left, right)
        movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # Create a queue for BFS and add the first position
        queue = [(pos1, [pos1])]
        # Create a set to store the visited positions
        visited = set()
        while queue:
            # Dequeue the current position and the path
            (current_pos, path) = queue.pop(0)
            # If the current position is the second position, return True
            if current_pos == pos2:
                return True
            # Mark the current position as visited
            visited.add(current_pos)
            # Check all possible movements
            for movement in movements:
                # Calculate the new position
                new_pos = (current_pos[0] + movement[0], current_pos[1] + movement[1])
                # Check if the new position is within the game board range and not visited
                if (0 <= new_pos[0] < self.BOARD_SIZE[0] and 0 <= new_pos[1] < self.BOARD_SIZE[1] and
                    new_pos not in visited):
                    # Check if the new position has the same icon or is empty
                    if self.board[new_pos[0]][new_pos[1]] == self.board[pos1[0]][pos1[1]] or self.board[new_pos[0]][new_pos[1]] == '':
                        # Add the new position to the queue
                        queue.append((new_pos, path + [new_pos]))
        return False

    def remove_icons(self, pos1, pos2):
        # Remove the connected icons on the game board
        self.board[pos1[0]][pos1[1]] = ''
        self.board[pos2[0]][pos2[1]] = ''

    def is_game_over(self):
        # Check if the game is over (i.e., if there are no more icons on the game board)
        for row in self.board:
            for icon in row:
                if icon != '':
                    return False
        return True