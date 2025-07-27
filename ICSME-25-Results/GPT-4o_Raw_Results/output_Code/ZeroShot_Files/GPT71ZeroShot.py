class PushBoxGame:
    def __init__(self, map):
        """
        Initialize the push box game with the map and various attributes.
        """
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
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] == 'P':  # Player start position
                    self.player_row = row
                    self.player_col = col
                elif self.map[row][col] == 'T':  # Target position
                    self.targets.append((row, col))
                    self.target_count += 1
                elif self.map[row][col] == 'B':  # Box position
                    self.boxes.append((row, col))

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        And update the value of self.is_game_over.
        :return self.is_game_over: True if all the boxes are placed on target positions, or False otherwise.
        """
        # Check if all boxes are on target positions
        on_target_count = 0
        for box in self.boxes:
            if box in self.targets:
                on_target_count += 1
        self.is_game_over = (on_target_count == self.target_count)
        return self.is_game_over

    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :return: True if the game is won, False otherwise.
        """
        # Define movement vectors
        direction_vectors = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }

        if direction in direction_vectors:
            # Calculate new player position
            d_row, d_col = direction_vectors[direction]
            new_player_row = self.player_row + d_row
            new_player_col = self.player_col + d_col

            # Check if new position is within bounds
            if 0 <= new_player_row < len(self.map) and 0 <= new_player_col < len(self.map[0]):
                # Check if new position is a box
                if (new_player_row, new_player_col) in self.boxes:
                    # Calculate new box position
                    new_box_row = new_player_row + d_row
                    new_box_col = new_player_col + d_col

                    # Check if box can be moved
                    if 0 <= new_box_row < len(self.map) and 0 <= new_box_col < len(self.map[0]) and self.map[new_box_row][new_box_col] != 'W' and (new_box_row, new_box_col) not in self.boxes:
                        # Move box
                        self.boxes.remove((new_player_row, new_player_col))
                        self.boxes.append((new_box_row, new_box_col))
                        # Move player
                        self.player_row = new_player_row
                        self.player_col = new_player_col
                elif self.map[new_player_row][new_player_col] != 'W':  # Check if new position is not a wall
                    # Move player
                    self.player_row = new_player_row
                    self.player_col = new_player_col

        # Check if the game is won after the move
        return self.check_win()