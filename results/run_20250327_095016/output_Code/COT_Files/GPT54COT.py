import random

class MahjongConnect:
    def __init__(self, BOARD_SIZE, ICONS):
        self.BOARD_SIZE = BOARD_SIZE
        self.ICONS = ICONS
        self.board = self.create_board()

    def create_board(self):
        num_pairs = (self.BOARD_SIZE[0] * self.BOARD_SIZE[1]) // 2
        icons = self.ICONS * (num_pairs // len(self.ICONS)) + self.ICONS[:num_pairs % len(self.ICONS)]
        icons = icons * 2
        random.shuffle(icons)
        
        board = []
        for i in range(self.BOARD_SIZE[0]):
            row = icons[i * self.BOARD_SIZE[1]:(i + 1) * self.BOARD_SIZE[1]]
            board.append(row)
        return board

    def is_valid_move(self, pos1, pos2):
        if pos1 == pos2:
            return False
        if not (0 <= pos1[0] < self.BOARD_SIZE[0] and 0 <= pos1[1] < self.BOARD_SIZE[1]):
            return False
        if not (0 <= pos2[0] < self.BOARD_SIZE[0] and 0 <= pos2[1] < self.BOARD_SIZE[1]):
            return False
        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False
        return self.has_path(pos1, pos2)

    def has_path(self, pos1, pos2):
        if pos1[0] == pos2[0]:
            row = pos1[0]
            start = min(pos1[1], pos2[1]) + 1
            end = max(pos1[1], pos2[1])
            if all(self.board[row][col] == ' ' for col in range(start, end)):
                return True
        elif pos1[1] == pos2[1]:
            col = pos1[1]
            start = min(pos1[0], pos2[0]) + 1
            end = max(pos1[0], pos2[0])
            if all(self.board[row][col] == ' ' for row in range(start, end)):
                return True
        return False

    def remove_icons(self, pos1, pos2):
        self.board[pos1[0]][pos1[1]] = ' '
        self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        for row in self.board:
            for icon in row:
                if icon != ' ':
                    return False
        return True