class Snake:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, food_position):
        """
        Initialize the length of the snake, screen width, screen height, block size, snake head position, score, and food position.
        """
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.BLOCK_SIZE = BLOCK_SIZE
        self.snake_body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = (0, 0)  # Initial direction is stationary
        self.food_position = food_position
        self.score = 0

    def move(self, direction):
        """
        Move the snake in the specified direction. If the new position of the snake's head is equal to the position of the food, then eat the food; If the position of the snake's head is equal to the position of its body, then start over, otherwise its own length plus one.
        :return: None
        """
        # Update the direction
        self.direction = direction

        # Calculate new head position
        head_x, head_y = self.snake_body[0]
        delta_x, delta_y = self.direction
        new_head = (head_x + delta_x * self.BLOCK_SIZE, head_y + delta_y * self.BLOCK_SIZE)

        # Check if new head position is the food position
        if new_head == self.food_position:
            self.eat_food()
        else:
            # Move the snake by removing the tail
            self.snake_body.pop()

        # Check if new head position is on the snake body (collision with itself)
        if new_head in self.snake_body:
            self.reset()
        else:
            # Add new head to the snake body
            self.snake_body.insert(0, new_head)

    def random_food_position(self):
        """
        Randomly generate a new food position, but don't place it on the snake.
        :return: None, Change the food position
        """
        while True:
            x = random.randint(0, (self.SCREEN_WIDTH // self.BLOCK_SIZE) - 1) * self.BLOCK_SIZE
            y = random.randint(0, (self.SCREEN_HEIGHT // self.BLOCK_SIZE) - 1) * self.BLOCK_SIZE
            new_food_position = (x, y)
            if new_food_position not in self.snake_body:
                self.food_position = new_food_position
                break

    def reset(self):
        """
        Reset the snake to its initial state. Set the length to 1, the snake head position to ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)), the score to 0, and randomly generate new food position.
        :return: None
        """
        self.snake_body = [(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2)]
        self.direction = (0, 0)
        self.score = 0
        self.random_food_position()

    def eat_food(self):
        """
        Increase the length of the snake by 1 and increase the score by 100. Randomly generate a new food position, but
        don't place it on the snake.
        :return: None
        """
        # Increase the length of the snake (by not removing the tail)
        self.snake_body.append(self.snake_body[-1])  # Add a new block at the tail position

        # Increase the score
        self.score += 100

        # Generate a new food position
        self.random_food_position()