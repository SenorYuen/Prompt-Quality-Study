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
        # Iterate through the map to find the player, targets, and boxes
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 'P':  # Player
                    self.player_row = i
                    self.player_col = j
                elif self.map[i][j] == 'T':  # Target
                    self.targets.append((i, j))
                    self.target_count += 1
                elif self.map[i][j] == 'B':  # Box
                    self.boxes.append((i, j))

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        And update the value of self.is_game_over.
        :return self.is_game_over: True if all the boxes are placed on target positions, or False otherwise.
        """
        # Check if all boxes are on target positions
        self.is_game_over = set(self.boxes).issubset(set(self.targets))
        return self.is_game_over

    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :return: True if the game is won, False otherwise.
        """
        # Define possible directions
        directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }

        # Calculate new player position
        new_row = self.player_row + directions[direction][0]
        new_col = self.player_col + directions[direction][1]

        # Check if new position is within the map boundaries
        if 0 <= new_row < len(self.map) and 0 <= new_col < len(self.map[0]):
            # Check if new position is a box
            if (new_row, new_col) in self.boxes:
                # Calculate new box position
                new_box_row = new_row + directions[direction][0]
                new_box_col = new_col + directions[direction][1]

                # Check if new box position is within the map boundaries and not a wall
                if 0 <= new_box_row < len(self.map) and 0 <= new_box_col < len(self.map[0]) and self.map[new_box_row][new_box_col] != 'W':
                    # Move the box
                    self.boxes.remove((new_row, new_col))
                    self.boxes.append((new_box_row, new_box_col))

                    # Move the player
                    self.player_row = new_row
                    self.player_col = new_col
                else:
                    # Cannot move the box, so do not move the player
                    pass
            elif self.map[new_row][new_col] != 'W':  # Not a wall
                # Move the player
                self.player_row = new_row
                self.player_col = new_col

        # Check if the game is won
        return self.check_win()