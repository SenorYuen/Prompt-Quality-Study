class EightPuzzle:
    def __init__(self, initial_state):
        # Initialize the initial state of the 8-puzzle game
        self.initial_state = initial_state
        # Set the goal state of the game (solved state)
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def find_blank(self, state):
        # Iterate over the 2D list to find the blank position (0)
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] == 0:
                    # Return the coordinates of the blank position
                    return i, j

    def move(self, state, direction):
        # Find the blank position
        i, j = self.find_blank(state)
        # Create a copy of the current state
        new_state = [row[:] for row in state]
        
        # Move the blank position according to the given direction
        if direction == 'up' and i > 0:
            new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        elif direction == 'down' and i < 2:
            new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
        elif direction == 'left' and j > 0:
            new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
        elif direction == 'right' and j < 2:
            new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
        
        # Return the new state
        return new_state

    def get_possible_moves(self, state):
        # Find the blank position
        i, j = self.find_blank(state)
        # Initialize a list to store possible moves
        moves = []
        
        # Check all possible directions
        if i > 0:
            moves.append('up')
        if i < 2:
            moves.append('down')
        if j > 0:
            moves.append('left')
        if j < 2:
            moves.append('right')
        
        # Return the list of possible moves
        return moves

    def solve(self):
        # Initialize a queue with the initial state
        open_list = [(self.initial_state, [])]
        # Initialize a set to store visited states
        visited = set()
        
        while open_list:
            # Dequeue the next state
            state, path = open_list.pop(0)
            # Convert the state to a tuple for hashing
            state_tuple = tuple(map(tuple, state))
            
            # Check if the state is the goal state
            if state == self.goal_state:
                # Return the path to the goal state
                return path
            
            # Check if the state has been visited
            if state_tuple in visited:
                continue
            
            # Mark the state as visited
            visited.add(state_tuple)
            
            # Get all possible moves from the current state
            for move in self.get_possible_moves(state):
                # Get the new state after making the move
                new_state = self.move(state, move)
                # Append the new state and the updated path to the queue
                open_list.append((new_state, path + [move]))
        
        # If no solution is found, return None
        return None

# Example usage:
if __name__ == "__main__":
    # Initialize the 8-puzzle game with a given initial state
    game = EightPuzzle([[4, 1, 3], [7, 2, 5], [0, 8, 6]])
    # Solve the puzzle
    solution = game.solve()
    print("Solution:", solution)