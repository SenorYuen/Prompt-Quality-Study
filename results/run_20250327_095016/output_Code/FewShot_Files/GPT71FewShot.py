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
        """
        Initialize the game by setting the positions of the player, targets, and boxes based on the map.
        """
        for r, row in enumerate(self.map):
            for c, char in enumerate(row):
                if char == 'O':
                    self.player_row, self.player_col = r, c
                elif char == 'G':
                    self.targets.append((r, c))
                    self.target_count += 1
                elif char == 'X':
                    self.boxes.append((r, c))

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        """
        if all(box in self.targets for box in self.boxes):
            self.is_game_over = True
        return self.is_game_over

    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        """
        if self.is_game_over:
            return True

        # Determine movement direction
        move_row, move_col = 0, 0
        if direction == 'w':  # Up
            move_row = -1
        elif direction == 's':  # Down
            move_row = 1
        elif direction == 'a':  # Left
            move_col = -1
        elif direction == 'd':  # Right
            move_col = 1

        new_row = self.player_row + move_row
        new_col = self.player_col + move_col

        # Check if the player can move to the new position
        if self.map[new_row][new_col] == '#':
            return False

        # Check if there is a box in the new position
        if (new_row, new_col) in self.boxes:
            box_new_row = new_row + move_row
            box_new_col = new_col + move_col

            # Check if the box can be moved
            if self.map[box_new_row][box_new_col] == '#' or (box_new_row, box_new_col) in self.boxes:
                return False

            # Move the box
            self.boxes.remove((new_row, new_col))
            self.boxes.append((box_new_row, box_new_col))

        # Move the player
        self.player_row, self.player_col = new_row, new_col

        # Check if the game is won
        return self.check_win()

    def print_map(self):
        """
        Print the current state of the map.
        """
        for r, row in enumerate(self.map):
            row_list = list(row)
            if (r, self.player_col) == (self.player_row, self.player_col):
                row_list[self.player_col] = 'O'
            for box in self.boxes:
                if (r, box[1]) == box:
                    row_list[box[1]] = 'X'
            print(''.join(row_list))