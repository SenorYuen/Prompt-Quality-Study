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
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 'O':
                    self.player_row = i
                    self.player_col = j
                elif self.map[i][j] == 'G':
                    self.targets.append((i, j))
                    self.target_count += 1
                elif self.map[i][j] == 'X':
                    self.boxes.append((i, j))

    def check_win(self):
        for box in self.boxes:
            if box not in self.targets:
                self.is_game_over = False
                return False
        self.is_game_over = True
        return True

    def move(self, direction):
        new_row = self.player_row
        new_col = self.player_col
        if direction == 'w':
            new_row -= 1
        elif direction == 's':
            new_row += 1
        elif direction == 'a':
            new_col -= 1
        elif direction == 'd':
            new_col += 1

        if self.map[new_row][new_col] == '#':
            return self.check_win()

        if (new_row, new_col) in self.boxes:
            box_row = new_row
            box_col = new_col
            new_box_row = box_row
            new_box_col = box_col
            if direction == 'w':
                new_box_row -= 1
            elif direction == 's':
                new_box_row += 1
            elif direction == 'a':
                new_box_col -= 1
            elif direction == 'd':
                new_box_col += 1

            if self.map[new_box_row][new_box_col] == '#':
                return self.check_win()

            if (new_box_row, new_box_col) in self.boxes:
                return self.check_win()

            self.boxes.remove((box_row, box_col))
            self.boxes.append((new_box_row, new_box_col))

        self.player_row = new_row
        self.player_col = new_col

        return self.check_win()