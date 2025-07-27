from collections import deque

class EightPuzzle:
    def __init__(self, initial_state):
        """
        Initializing the initial state of Eight Puzzle Game, stores in attribute self.initial_state.
        And set the goal state of this game, stores in self.goal_state. In this case, set the size as 3*3
        """
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Goal state for 8-puzzle

    def find_blank(self, state):
        """
        Find the blank position of current state, which is the 0 element.
        :return i, j: two Integers, represent the coordinate of the blank block.
        """
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def move(self, state, direction):
        """
        Find the blank block, then makes the board move toward the given direction.
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        """
        i, j = self.find_blank(state)
        new_state = [row[:] for row in state]  # Create a deep copy of the state
        
        if direction == 'up' and i > 0:
            new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        elif direction == 'down' and i < 2:
            new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
        elif direction == 'left' and j > 0:
            new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
        elif direction == 'right' and j < 2:
            new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
        
        return new_state

    def get_possible_moves(self, state):
        """
        According to the current state, find all the possible moving directions. Only has 4 directions 'up', 'down', 'left', 'right'.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        """
        moves = []
        i, j = self.find_blank(state)
        
        if i > 0:
            moves.append('up')
        if i < 2:
            moves.append('down')
        if j > 0:
            moves.append('left')
        if j < 2:
            moves.append('right')
        
        return moves

    def solve(self):
        """
        Use BFS algorithm to find the path solution which makes the initial state to the goal method.
        Maintain a list as a queue, named as open_list, append the initial state.
        Always visit and pop the 0 index element, invoke get_possible_moves method to find all the possible directions.
        Traverse the possible_moves list and invoke move method to get several new states. Then append them.
        Redo the above steps until the open_list is empty or the state has changed to the goal state.
        :return path: list of str, the solution to the goal state.
        """
        open_list = deque([(self.initial_state, [])])
        visited = set()
        
        while open_list:
            current_state, path = open_list.popleft()
            visited.add(tuple(map(tuple, current_state)))
            
            if current_state == self.goal_state:
                return path
            
            for move in self.get_possible_moves(current_state):
                new_state = self.move(current_state, move)
                new_state_tuple = tuple(map(tuple, new_state))
                
                if new_state_tuple not in visited:
                    open_list.append((new_state, path + [move]))
                    visited.add(new_state_tuple)
        
        return None  # Return None if no solution is found