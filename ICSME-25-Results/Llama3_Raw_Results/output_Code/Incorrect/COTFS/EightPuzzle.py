class EightPuzzle:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def find_blank(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def move(self, state, direction):
        i, j = self.find_blank(state)
        new_state = [row[:] for row in state]
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
        i, j = self.find_blank(state)
        moves = []
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
        open_list = [(self.initial_state, [])]
        while open_list:
            state, path = open_list.pop(0)
            if state == self.goal_state:
                return path
            for direction in self.get_possible_moves(state):
                new_state = self.move(state, direction)
                open_list.append((new_state, path + [direction]))
        return None