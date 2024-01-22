# --- Day 2: Bathroom Security ---

directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}


def solve_part_1(data):
    keypad = [[1,2,3], [4,5,6], [7,8,9]]
    code = ""
    r, c = 0, 0
    for line in data:
        for d in line:
            r = max(min(2, r + directions[d][0]), 0)
            c = max(min(2, c + directions[d][1]), 0)
        code += str(keypad[r][c])
            
    print(code)


def solve_part_2(data):
    keypad = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, '1', 0, 0, 0],
        [0, 0, '2', '3', '4', 0, 0],
        [0, '5', '6', '7', '8', '9', 0],
        [0, 0, 'A', 'B', 'C', 0, 0], 
        [0, 0, 0, 'D', 0, 0 , 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    R, C = len(keypad), len(keypad[0])
    code = ""
    r, c = 3, 1
    for line in data:
        for d in line:
            new_r = r + directions[d][0]
            new_c = c + directions[d][1]
            if new_r < 0 or new_r >= R :
                continue
            if new_c < 0 or new_c >= C:
                continue
            if keypad[new_r][new_c] != 0:
                r, c = new_r, new_c
        code += keypad[r][c]
            
    print(code)



if __name__ == '__main__':

    data = open(0).read().splitlines()
    
    solve_part_1(data)
    solve_part_2(data)