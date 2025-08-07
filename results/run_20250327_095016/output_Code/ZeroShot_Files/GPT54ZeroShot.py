import random

class MahjongConnect:
    def __init__(self, BOARD_SIZE, ICONS):
        """
        Initialize the board size and the icon list, create the game board.
        """
        self.BOARD_SIZE = BOARD_SIZE
        self.ICONS = ICONS
        self.board = self.create_board()

    def create_board(self):
        """
        Create the game board with the given board size and icons.
        :return: 2-dimensional list, the game board
        """
        # Calculate the total number of icons needed
        total_icons = self.BOARD_SIZE * self.BOARD_SIZE
        # Ensure there are pairs of icons
        if total_icons % 2 != 0:
            raise ValueError("The board size must allow for pairs of icons.")
        
        # Create pairs of icons
        icon_pairs = (self.ICONS * (total_icons // len(self.ICONS) // 2)) * 2
        random.shuffle(icon_pairs)
        
        # Create the board as a 2D list
        board = [icon_pairs[i:i + self.BOARD_SIZE] for i in range(0, total_icons, self.BOARD_SIZE)]
        return board

    def is_valid_move(self, pos1, pos2):
        """
        Check if the move of two icons is valid.
        :return: True or False, representing whether the move of two icons is valid
        """
        x1, y1 = pos1
        x2, y2 = pos2

        # Check if positions are within the board range
        if not (0 <= x1 < self.BOARD_SIZE and 0 <= y1 < self.BOARD_SIZE and
                0 <= x2 < self.BOARD_SIZE and 0 <= y2 < self.BOARD_SIZE):
            return False

        # Check if the two positions are not the same
        if pos1 == pos2:
            return False

        # Check if the two positions have the same icon
        if self.board[x1][y1] != self.board[x2][y2]:
            return False

        # Check if there is a valid path between the two positions
        return self.has_path(pos1, pos2)

    def has_path(self, pos1, pos2):
        """
        Check if there is a path between two icons.
        :return: True or False, representing whether there is a path between two icons
        """
        # For simplicity, assume a direct path is available if positions are adjacent
        x1, y1 = pos1
        x2, y2 = pos2

        # Check for direct adjacency (horizontal or vertical)
        if (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1):
            return True

        # Implement more complex path finding logic here if needed
        return False

    def remove_icons(self, pos1, pos2):
        """
        Remove the connected icons on the game board.
        :return: None
        """
        x1, y1 = pos1
        x2, y2 = pos2

        # Set the positions to None to indicate removal
        self.board[x1][y1] = None
        self.board[x2][y2] = None

    def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board).
        :return: True or False, representing whether the game is over
        """
        # Check if all positions on the board are None
        for row in self.board:
            for icon in row:
                if icon is not None:
                    return False
        return True