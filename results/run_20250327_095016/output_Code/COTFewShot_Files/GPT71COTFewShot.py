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

        move_delta = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
        if direction not in move_delta:
            return False

        dr, dc = move_delta[direction]
        new_player_row = self.player_row + dr
        new_player_col = self.player_col + dc

        # Check if the player is moving into a wall
        if self.map[new_player_row][new_player_col] == '#':
            return False

        # Check if the player is moving into a box
        if (new_player_row, new_player_col) in self.boxes:
            new_box_row = new_player_row + dr
            new_box_col = new_player_col + dc

            # Check if the box can be moved (i.e., not moving into a wall or another box)
            if self.map[new_box_row][new_box_col] == '#' or (new_box_row, new_box_col) in self.boxes:
                return False

            # Move the box
            self.boxes.remove((new_player_row, new_player_col))
            self.boxes.append((new_box_row, new_box_col))

        # Move the player
        self.player_row = new_player_row
        self.player_col = new_player_col

        return self.check_win()