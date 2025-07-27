import random

class Snake:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, food_position):
        # Initialize the length of the snake
        self.length = 1
        # Initialize the screen width, screen height, and block size
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.BLOCK_SIZE = BLOCK_SIZE
        # Initialize the snake head position to the center of the screen
        self.snake_head_position = [(SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2)]
        # Initialize the snake body positions
        self.snake_body_positions = [[(SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2)]]
        # Initialize the score
        self.score = 0
        # Initialize the food position
        self.food_position = food_position
        # Initialize the direction
        self.direction = 'right'

    def move(self, direction):
        # Update the direction
        self.direction = direction
        # Calculate the new head position based on the direction
        if direction == 'right':
            new_head_position = [self.snake_head_position[0] + self.BLOCK_SIZE, self.snake_head_position[1]]
        elif direction == 'left':
            new_head_position = [self.snake_head_position[0] - self.BLOCK_SIZE, self.snake_head_position[1]]
        elif direction == 'up':
            new_head_position = [self.snake_head_position[0], self.snake_head_position[1] - self.BLOCK_SIZE]
        elif direction == 'down':
            new_head_position = [self.snake_head_position[0], self.snake_head_position[1] + self.BLOCK_SIZE]
        
        # Check if the new head position is equal to the food position
        if new_head_position == self.food_position:
            # Eat the food
            self.eat_food()
        else:
            # Remove the last body position if the snake has not eaten food
            if len(self.snake_body_positions) >= self.length:
                self.snake_body_positions.pop(0)
        
        # Update the snake head position
        self.snake_head_position = new_head_position
        # Add the new head position to the snake body positions
        self.snake_body_positions.append(self.snake_head_position[:])
        
        # Check if the snake has collided with its body
        if self.snake_head_position in self.snake_body_positions[:-1]:
            # Reset the snake
            self.reset()

    def random_food_position(self):
        # Randomly generate a new food position
        while True:
            new_food_position = [random.randint(0, self.SCREEN_WIDTH - self.BLOCK_SIZE) // self.BLOCK_SIZE * self.BLOCK_SIZE, 
                                 random.randint(0, self.SCREEN_HEIGHT - self.BLOCK_SIZE) // self.BLOCK_SIZE * self.BLOCK_SIZE]
            # Check if the new food position is not on the snake
            if new_food_position not in self.snake_body_positions:
                self.food_position = new_food_position
                break

    def reset(self):
        # Reset the length to 1
        self.length = 1
        # Reset the snake head position to the center of the screen
        self.snake_head_position = [(self.SCREEN_WIDTH // 2), (self.SCREEN_HEIGHT // 2)]
        # Reset the snake body positions
        self.snake_body_positions = [[(self.SCREEN_WIDTH // 2), (self.SCREEN_HEIGHT // 2)]]
        # Reset the score
        self.score = 0
        # Randomly generate a new food position
        self.random_food_position()

    def eat_food(self):
        # Increase the length of the snake by 1
        self.length += 1
        # Increase the score by 100
        self.score += 100
        # Randomly generate a new food position
        self.random_food_position()