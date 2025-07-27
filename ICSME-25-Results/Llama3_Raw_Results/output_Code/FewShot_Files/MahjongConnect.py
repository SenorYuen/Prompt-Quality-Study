import random

class MahjongConnect:
    """
    MahjongConnect is a class representing a game board for Mahjong Connect with features like creating the board, checking valid moves, finding paths, removing icons, and checking if the game is over.
    """

    def __init__(self, BOARD_SIZE, ICONS):
        """
        initialize the board size and the icon list, create the game board
        :param BOARD_SIZE: list of two integer numbers, representing the number of rows and columns of the game board
        :param ICONS: list of string, representing the icons
        """
        self.BOARD_SIZE = BOARD_SIZE
        self.ICONS = ICONS
        self.board = self.create_board()

    def create_board(self):
        """
        create the game board with the given board size and icons
        :return: 2-dimensional list, the game board
        """
        # Initialize an empty board with the given size
        board = [[None for _ in range(self.BOARD_SIZE[1])] for _ in range(self.BOARD_SIZE[0])]
        
        # Fill the board with random icons
        for i in range(self.BOARD_SIZE[0]):
            for j in range(self.BOARD_SIZE[1]):
                board[i][j] = random.choice(self.ICONS)
        
        return board

    def is_valid_move(self, pos1, pos2):
        """
        check if the move of two icons is valid (i.e. positions are within the game board range, the two positions are not the same, the two positions have the same icon, and there is a valid path between the two positions)
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return:True or False ,representing whether the move of two icons is valid
        """
        # Check if positions are within the game board range
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
        return self.has_path(pos1, pos2)

    def has_path(self, pos1, pos2):
        """
        check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False ,representing whether there is a path between two icons
        """
        # Define the possible movements (up, down, left, right)
        movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Perform a breadth-first search to find a path
        queue = [(pos1, [pos1])]
        while queue:
            (node, path) = queue.pop(0)
            for movement in movements:
                new_pos = (node[0] + movement[0], node[1] + movement[1])
                if (0 <= new_pos[0] < self.BOARD_SIZE[0] and 0 <= new_pos[1] < self.BOARD_SIZE[1] and
                    new_pos not in path):
                    if new_pos == pos2:
                        return True
                    queue.append((new_pos, path + [new_pos]))
        
        return False

    def remove_icons(self, pos1, pos2):
        """
        remove the connected icons on the game board
        :param pos1: position tuple(x, y) of the first icon to be removed
        :param pos2: position tuple(x, y) of the second icon to be removed
        :return: None
        """
        # Remove the icons at the given positions
        self.board[pos1[0]][pos1[1]] = None
        self.board[pos2[0]][pos2[1]] = None
        
        # Drop down the icons above the removed icons
        for j in range(self.BOARD_SIZE[1]):
            column = [self.board[i][j] for i in range(self.BOARD_SIZE[0])]
            column = [icon for icon in column if icon is not None]
            column += [None] * (self.BOARD_SIZE[0] - len(column))
            for i in range(self.BOARD_SIZE[0]):
                self.board[i][j] = column[i]

    def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board)
        :return: True or False ,representing whether the game is over
        """
        # Check if there are any icons left on the board
        for row in self.board:
            for icon in row:
                if icon is not None:
                    return False
        
        return True