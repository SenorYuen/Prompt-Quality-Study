import random

class Snake:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, food_position):
        self.length = 1
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.BLOCK_SIZE = BLOCK_SIZE
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.score = 0
        self.food_position = food_position

    def move(self, direction):
        current_head = self.positions[0]
        new_head = (current_head[0] + direction[0] * self.BLOCK_SIZE,
                    current_head[1] + direction[1] * self.BLOCK_SIZE)
        
        if new_head == self.food_position:
            self.eat_food()
        else:
            if new_head in self.positions:
                self.reset()
                return
            self.positions = [new_head] + self.positions[:-1]

    def random_food_position(self):
        while True:
            new_position = (random.randint(0, (self.SCREEN_WIDTH // self.BLOCK_SIZE) - 1) * self.BLOCK_SIZE,
                            random.randint(0, (self.SCREEN_HEIGHT // self.BLOCK_SIZE) - 1) * self.BLOCK_SIZE)
            if new_position not in self.positions:
                self.food_position = new_position
                break

    def reset(self):
        self.length = 1
        self.positions = [((self.SCREEN_WIDTH / 2), (self.SCREEN_HEIGHT / 2))]
        self.score = 0
        self.random_food_position()

    def eat_food(self):
        self.length += 1
        self.score += 10
        self.positions.append(self.positions[-1])
        self.random_food_position()