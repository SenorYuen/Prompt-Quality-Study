class PushBoxGame:
    """
    This class implements a functionality of a sokoban game, where the player needs to move boxes to designated targets in order to win.
    """

    def __init__(self, map):
        """
        Initialize the push box game with the map and various attributes.
        :param map: list[str], the map of the push box game, represented as a list of strings. 
            Each character on the map represents a different element, including the following:
            - '#' represents a wall that neither the player nor the box can pass through;
            - 'O' represents the initial position of the player;
            - 'G' represents the target position;
            - 'X' represents the initial position of the box.
        >>> map = ["#####", "#O  #", "# X #", "#  G#", "#####"]   
        >>> game = PushBoxGame(map)                
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
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.targets
        [(3, 3)]
        >>> game.boxes
        [(2, 2)]
        >>> game.player_row
        1
        >>> game.player_col
        1
        """
        # Iterate over each row and column in the map
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                # Check if the current position is the player
                if self.map[row][col] == 'O':
                    self.player_row = row
                    self.player_col = col
                # Check if the current position is a target
                elif self.map[row][col] == 'G':
                    self.targets.append((row, col))
                    self.target_count += 1
                # Check if the current position is a box
                elif self.map[row][col] == 'X':
                    self.boxes.append((row, col))

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        And update the value of self.is_game_over.
        :return self.is_game_over: True if all the boxes are placed on target positions, or False otherwise.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.check_win()
        """
        # Check if all boxes are on target positions
        for box in self.boxes:
            if box not in self.targets:
                self.is_game_over = False
                return self.is_game_over
        self.is_game_over = True
        return self.is_game_over

    def print_map(self):
        """
        Print the current state of the game map.
        """
        # Create a copy of the map to avoid modifying the original map
        game_map = [list(row) for row in self.map]
        # Update the player position on the map
        game_map[self.player_row][self.player_col] = 'O'
        # Update the box positions on the map
        for box in self.boxes:
            game_map[box[0]][box[1]] = 'X'
        # Print the updated map
        for row in game_map:
            print(' '.join(row))

    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :param direction: str, the direction of the player's movement. 
            It can be 'w', 's', 'a', or 'd' representing up, down, left, or right respectively.

        :return: True if the game is won, False otherwise.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])       
        >>> game.print_map()
        # # # # # 
        # O     #
        #   X   #
        #     G #
        # # # # #
        >>> game.move('d')
        False
        >>> game.move('s')   
        False
        >>> game.move('a')   
        False
        >>> game.move('s') 
        False
        >>> game.move('d') 
        True
        """
        # Get the new player position based on the direction
        new_row, new_col = self.player_row, self.player_col
        if direction == 'w':
            new_row -= 1
        elif direction == 's':
            new_row += 1
        elif direction == 'a':
            new_col -= 1
        elif direction == 'd':
            new_col += 1

        # Check if the new position is a wall
        if self.map[new_row][new_col] == '#':
            return self.check_win()

        # Check if the new position is a box
        if (new_row, new_col) in self.boxes:
            # Get the new box position
            new_box_row, new_box_col = new_row, new_col
            if direction == 'w':
                new_box_row -= 1
            elif direction == 's':
                new_box_row += 1
            elif direction == 'a':
                new_box_col -= 1
            elif direction == 'd':
                new_box_col += 1

            # Check if the new box position is a wall or another box
            if self.map[new_box_row][new_box_col] == '#' or (new_box_row, new_box_col) in self.boxes:
                return self.check_win()

            # Update the box position
            self.boxes.remove((new_row, new_col))
            self.boxes.append((new_box_row, new_box_col))

        # Update the player position
        self.player_row, self.player_col = new_row, new_col

        return self.check_win()