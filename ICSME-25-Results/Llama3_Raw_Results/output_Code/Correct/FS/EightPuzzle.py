class EightPuzzle:
    """
    This class is an implementation of the classic 8-puzzle game, including methods for finding the blank tile, making moves, getting possible moves, and solving the puzzle using a breadth-first search algorithm.
    """

    def __init__(self, initial_state):
        """
        Initializing the initial state of Eight Puzzle Game, stores in attribute self.initial_state.
        And set the goal state of this game, stores in self.goal_state. In this case, set the size as 3*3
        :param initial_state: a 3*3 size list of Integer, stores the initial state
        """
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def find_blank(self, state):
        """
        Find the blank position of current state, which is the 0 element.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return i, j: two Integers, represent the coordinate of the blank block.
        """
        # Iterate over each row and column in the state to find the blank tile (0)
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    # Return the coordinates of the blank tile
                    return i, j

    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        """
        # Find the coordinates of the blank tile
        i, j = self.find_blank(state)
        
        # Create a copy of the current state to avoid modifying the original state
        new_state = [row[:] for row in state]
        
        # Move the blank tile according to the given direction
        if direction == 'up' and i > 0:
            # Swap the blank tile with the tile above it
            new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        elif direction == 'down' and i < 2:
            # Swap the blank tile with the tile below it
            new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
        elif direction == 'left' and j > 0:
            # Swap the blank tile with the tile to its left
            new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
        elif direction == 'right' and j < 2:
            # Swap the blank tile with the tile to its right
            new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
        
        # Return the new state after moving the blank tile
        return new_state

    def get_possible_moves(self, state):
        """
        According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        """
        # Find the coordinates of the blank tile
        i, j = self.find_blank(state)
        
        # Initialize an empty list to store the possible moves
        moves = []
        
        # Check if the blank tile can move up
        if i > 0:
            moves.append('up')
        # Check if the blank tile can move down
        if i < 2:
            moves.append('down')
        # Check if the blank tile can move left
        if j > 0:
            moves.append('left')
        # Check if the blank tile can move right
        if j < 2:
            moves.append('right')
        
        # Return the list of possible moves
        return moves

    def solve(self):
        """
        Use BFS algorithm to find the path solution which makes the initial state to the goal method.
        Maintain a list as a queue, named as open_list, append the initial state.
        Always visit and pop the 0 index element, invoke get_possible_moves method find all the possible directions.
        Traversal the possible_moves list and invoke move method to get several new states.Then append them.
        redo the above steps until the open_list is empty or the state has changed to the goal state.
        :return path: list of str, the solution to the goal state.
        """
        # Initialize the open list with the initial state
        open_list = [(self.initial_state, [])]
        
        # Initialize the closed list to keep track of visited states
        closed_list = []
        
        # Loop until the open list is empty
        while open_list:
            # Dequeue the first state from the open list
            state, path = open_list.pop(0)
            
            # Check if the current state is the goal state
            if state == self.goal_state:
                # Return the path to the goal state
                return path
            
            # Add the current state to the closed list
            closed_list.append(state)
            
            # Get the possible moves from the current state
            possible_moves = self.get_possible_moves(state)
            
            # Loop through each possible move
            for move in possible_moves:
                # Get the new state after making the move
                new_state = self.move(state, move)
                
                # Check if the new state has not been visited before
                if new_state not in closed_list:
                    # Add the new state to the open list with the updated path
                    open_list.append((new_state, path + [move]))
        
        # If the open list is empty and no solution is found, return None
        return None