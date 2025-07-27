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
        self.is_game_over = all(box in self.targets for box in self.boxes)
        return self.is_game_over

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
            return False

        if (new_row, new_col) in self.boxes:
            box_new_row = new_row
            box_new_col = new_col
            if direction == 'w':
                box_new_row -= 1
            elif direction == 's':
                box_new_row += 1
            elif direction == 'a':
                box_new_col -= 1
            elif direction == 'd':
                box_new_col += 1

            if self.map[box_new_row][box_new_col] == '#':
                return False
            elif (box_new_row, box_new_col) in self.boxes:
                return False

            self.boxes.remove((new_row, new_col))
            self.boxes.append((box_new_row, box_new_col))

        self.player_row = new_row
        self.player_col = new_col

        return self.check_win()