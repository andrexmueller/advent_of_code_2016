# --- Day 1: No Time for a Taxicab ---


def solve_part_1(data):
    position = [0, 0]
    current_dir = 'N'
    directions = {'NR': (0, 1, 'E'), 'NL': (0, -1, 'W'), 'SR': (0, -1, 'W'), 'SL': (0, 1, 'E'),
                  'ER': (1, 0, 'S'), 'EL': (-1, 0, 'N'), 'WR': (-1, 0, 'N'), 'WL': (1, 0, 'S')}
    for line in data:
        d, s = line[0], int(line[1:])
        position[0] += directions[current_dir+d][0] * s
        position[1] += directions[current_dir+d][1] * s
        current_dir = directions[current_dir+d][2]
        
    print(sum(map(abs, position)))


def solve_part_2(data):
    position = [0, 0]
    visited = set((0, 0))
    current_dir = 'N'
    directions = {'NR': (0, 1, 'E'), 'NL': (0, -1, 'W'), 'SR': (0, -1, 'W'), 'SL': (0, 1, 'E'),
                  'ER': (1, 0, 'S'), 'EL': (-1, 0, 'N'), 'WR': (-1, 0, 'N'), 'WL': (1, 0, 'S')}
    for line in data:
        d, s = line[0], int(line[1:])
        #print(s)
        for _ in range(s):
            position[0] += directions[current_dir+d][0]
            position[1] += directions[current_dir+d][1]
            if tuple(position) in visited:
                print(sum(map(abs, position)))
                return
            visited.add(tuple(position))
        current_dir = directions[current_dir+d][2]
            

# p2: 257 wrong
if __name__ == '__main__':

    data = open(0).read().split(', ')

    solve_part_1(data)
    solve_part_2(data)