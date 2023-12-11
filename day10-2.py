with open('input.txt') as f:
    read_data = f.read().strip().split('\n')


class PipeLoop:
    def __init__(self, inp):
        self.map = inp
        self.directions = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
        self.pipe_directions = {
            ('L', 'left'): 'up',
            ('F', 'up'): 'right',
            ('7', 'right'): 'down',
            ('J', 'down'): 'left',
            ('F', 'left'): 'down',
            ('7', 'up'): 'left',
            ('J', 'right'): 'up',
            ('L', 'down'): 'right',
            ('-', 'left'): 'left',
            ('-', 'right'): 'right',
            ('|', 'up'): 'up',
            ('|', 'down'): 'down',
        }
        self.start = self.find_start_point()
        self.loop = self.map_loop()
        self.enclosed = self.find_enclosed()

    def find_start_point(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == 'S':
                    return i, j

    def traversing(self, current_pipe, current_direction):
        (i, j) = current_pipe
        next_direction = self.pipe_directions[(self.map[i][j], current_direction)]
        next_pipe = tuple(map(sum, zip(current_pipe, self.directions[next_direction])))
        return next_pipe, next_direction

    def from_start_point(self):
        for d in self.directions:
            (di, dj) = tuple(map(sum, zip(self.start, self.directions[d])))
            if (self.map[di][dj], d) in self.pipe_directions:
                return (di, dj), d

    def map_loop(self):
        current, d = self.from_start_point()
        (i, j) = current
        loop = {current: (self.map[i][j], d)}
        while current != self.start:
            current, d = self.traversing(current, d)
            (i, j) = current
            loop[current] = self.map[i][j], d
        # Replace 'S'
        else:
            for p in ('L', 'F', '7', 'J', '|', '-'):
                if (p, d) in self.pipe_directions:
                    next_direction = self.pipe_directions[(p, d)]
                    next_pipe = tuple(map(sum, zip(current, self.directions[next_direction])))
                    if next_pipe == list(loop)[0]:
                        loop[current] = (p, d)
                        return loop

    # Part 2
    def find_enclosed(self):
        enclosed = set()
        inside_loop = {}
        loop_direction = 0
        # Get loop's direction
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if (i, j) in self.loop:
                    if self.loop[(i, j)][1] == 'up' or self.pipe_directions[self.loop[(i, j)]] == 'up':
                        loop_direction = 'up'
                    elif self.loop[(i, j)][1] == 'down' or self.pipe_directions[self.loop[(i, j)]] == 'down':
                        loop_direction = 'down'
                    # Get most outside loop's direction to check
                    if inside_loop == {}:
                        inside_loop = {loop_direction: True}
                elif loop_direction in inside_loop:
                    enclosed.add((i, j))
        return enclosed


pipes = PipeLoop(read_data)
print('Part 1:', len(pipes.loop) // 2)
print('Part 2:', len(pipes.enclosed))
