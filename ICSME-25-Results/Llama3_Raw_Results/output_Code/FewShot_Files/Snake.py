class Snake:
    """
    The class is a snake game, with allows snake to move and eat food, and also enables to reset, and generate a random food position.
    """

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, food_position):
        """
        Initialize the length of the snake, screen width, screen height, block size, snake head position, score, and food position.
        :param SCREEN_WIDTH: int
        :param SCREEN_HEIGHT: int
        :param BLOCK_SIZE: int, Size of moving units
        :param food_position: tuple, representing the position(x, y) of food.
        """
        self.length = 1
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.BLOCK_SIZE = BLOCK_SIZE
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.score = 0
        self.food_position = food_position
        # Initialize the direction of the snake
        self.direction = (0, 0)

    def move(self, direction):
        """
        Move the snake in the specified direction. If the new position of the snake's head is equal to the position of the food, then eat the food; If the position of the snake's head is equal to the position of its body, then start over, otherwise its own length plus one.
        :param direction: tuple, representing the direction of movement (x, y).
        :return: None
        """
        # Update the direction of the snake
        self.direction = direction
        # Calculate the new head position
        new_head_position = (self.positions[-1][0] + self.direction[0] * self.BLOCK_SIZE, self.positions[-1][1] + self.direction[1] * self.BLOCK_SIZE)
        
        # Check if the new head position is out of the screen
        if (new_head_position[0] < 0 or new_head_position[0] >= self.SCREEN_WIDTH or 
            new_head_position[1] < 0 or new_head_position[1] >= self.SCREEN_HEIGHT):
            self.reset()
            return
        
        # Check if the new head position is equal to the position of the food
        if new_head_position == self.food_position:
            self.eat_food()
        else:
            # Check if the new head position is equal to the position of its body
            if new_head_position in self.positions:
                self.reset()
                return
            # Update the positions of the snake
            self.positions.append(new_head_position)
            if len(self.positions) > self.length:
                self.positions.pop(0)

    def random_food_position(self):
        """
        Randomly generate a new food position, but don't place it on the snake.
        :return: None, Change the food position
        """
        # Generate a random position
        while True:
            x = random.randint(0, self.SCREEN_WIDTH - self.BLOCK_SIZE) // self.BLOCK_SIZE * self.BLOCK_SIZE
            y = random.randint(0, self.SCREEN_HEIGHT - self.BLOCK_SIZE) // self.BLOCK_SIZE * self.BLOCK_SIZE
            new_food_position = (x, y)
            # Check if the new food position is not on the snake
            if new_food_position not in self.positions:
                self.food_position = new_food_position
                break

    def reset(self):
        """
        Reset the snake to its initial state. Set the length to 1, the snake head position to ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)), the score to 0, and randomly generate new food position.
        :return: None
        """
        self.length = 1
        self.positions = [((self.SCREEN_WIDTH / 2), (self.SCREEN_HEIGHT / 2))]
        self.score = 0
        self.random_food_position()

    def eat_food(self):
        """
        Increase the length of the snake by 1 and increase the score by 100. Randomly generate a new food position, but
        don't place it on the snake.
        :return: None
        """
        self.length += 1
        self.score += 100
        self.random_food_position()