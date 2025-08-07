import random

class MahjongConnect:
    def __init__(self, BOARD_SIZE, ICONS):
        self.BOARD_SIZE = BOARD_SIZE
        self.ICONS = ICONS
        self.board = self.create_board()

    def create_board(self):
        rows, cols = self.BOARD_SIZE
        total_icons = rows * cols
        icons_needed = total_icons // 2
        icons_list = (self.ICONS * (icons_needed // len(self.ICONS) + 1))[:icons_needed] * 2
        random.shuffle(icons_list)
        return [icons_list[i * cols:(i + 1) * cols] for i in range(rows)]

    def is_valid_move(self, pos1, pos2):
        if pos1 == pos2:
            return False
        if not self.is_within_bounds(pos1) or not self.is_within_bounds(pos2):
            return False
        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False
        if not self.has_path(pos1, pos2):
            return False
        return True

    def is_within_bounds(self, pos):
        return 0 <= pos[0] < self.BOARD_SIZE[0] and 0 <= pos[1] < self.BOARD_SIZE[1]

    def has_path(self, pos1, pos2):
        # This is a simplified placeholder for path checking logic
        return True

    def remove_icons(self, pos1, pos2):
        if self.is_valid_move(pos1, pos2):
            self.board[pos1[0]][pos1[1]] = ' '
            self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        return all(icon == ' ' for row in self.board for icon in row)