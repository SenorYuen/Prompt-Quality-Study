class PushBoxGame:
    def __init__(self, map):
        self.map = map
        self.player_row = 0
        self.player_col = 0
        self.targets = []
        self.boxes = []
        self.target_count = 0
        self.is_game_over = False
        self.init_game()

    def init_game(self):
        for r, row in enumerate(self.map):
            for c, char in enumerate(row):
                if char == 'O':
                    self.player_row = r
                    self.player_col = c
                elif char == 'G':
                    self.targets.append((r, c))
                    self.target_count += 1
                elif char == 'X':
                    self.boxes.append((r, c))

    def check_win(self):
        for box in self.boxes:
            if box not in self.targets:
                self.is_game_over = False
                return False
        self.is_game_over = True
        return True

    def move(self, direction):
        if self.is_game_over:
            return True

        dir_map = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
        if direction not in dir_map:
            return False

        delta_row, delta_col = dir_map[direction]
        new_row = self.player_row + delta_row
        new_col = self.player_col + delta_col

        if self.map[new_row][new_col] == '#':
            return False

        if (new_row, new_col) in self.boxes:
            box_new_row = new_row + delta_row
            box_new_col = new_col + delta_col
            if self.map[box_new_row][box_new_col] == '#' or (box_new_row, box_new_col) in self.boxes:
                return False
            self.boxes.remove((new_row, new_col))
            self.boxes.append((box_new_row, box_new_col))

        self.player_row = new_row
        self.player_col = new_col

        return self.check_win()