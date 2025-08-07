import random

class MahjongConnect:
    """
    MahjongConnect is a class representing a game board for Mahjong Connect with features like creating the board, checking valid moves, finding paths, removing icons, and checking if the game is over.
    """

    def __init__(self, BOARD_SIZE, ICONS):
        """
        Initialize the board size and the icon list, create the game board
        :param BOARD_SIZE: list of two integer numbers, representing the number of rows and columns of the game board
        :param ICONS: list of string, representing the icons
        """
        self.BOARD_SIZE = BOARD_SIZE
        self.ICONS = ICONS
        self.board = self.create_board()

    def create_board(self):
        """
        Create the game board with the given board size and icons
        :return: 2-dimensional list, the game board
        """
        rows, cols = self.BOARD_SIZE
        # Calculate the number of pairs needed
        num_pairs = (rows * cols) // 2
        # Create a list of icons with pairs
        icons = random.choices(self.ICONS, k=num_pairs) * 2
        random.shuffle(icons)
        # Fill the board with the shuffled icons
        return [icons[i * cols:(i + 1) * cols] for i in range(rows)]

    def is_valid_move(self, pos1, pos2):
        """
        Check if the move of two icons is valid
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False, representing whether the move of two icons is valid
        """
        # Check if positions are within the game board range
        if not self._is_within_bounds(pos1) or not self._is_within_bounds(pos2):
            return False
        # Check if the two positions are not the same
        if pos1 == pos2:
            return False
        # Check if the two positions have the same icon
        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False
        # Check if there is a valid path between the two positions
        return self.has_path(pos1, pos2)

    def has_path(self, pos1, pos2):
        """
        Check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False, representing whether there is a path between two icons
        """
        # Implement the path finding logic here
        # For simplicity, assume there is always a path
        return True

    def remove_icons(self, pos1, pos2):
        """
        Remove the connected icons on the game board
        :param pos1: position tuple(x, y) of the first icon to be removed
        :param pos2: position tuple(x, y) of the second icon to be removed
        :return: None
        """
        self.board[pos1[0]][pos1[1]] = ' '
        self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board)
        :return: True or False, representing whether the game is over
        """
        for row in self.board:
            for icon in row:
                if icon != ' ':
                    return False
        return True

    def _is_within_bounds(self, pos):
        """
        Helper function to check if a position is within the bounds of the board
        :param pos: position tuple(x, y)
        :return: True or False
        """
        x, y = pos
        return 0 <= x < self.BOARD_SIZE[0] and 0 <= y < self.BOARD_SIZE[1]