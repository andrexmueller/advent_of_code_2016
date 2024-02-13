# Day 8: Two-Factor Authentication


def turn_on_rect(tall: int, wide: int) -> None:
    for r in range(tall):
        for c in range(wide):
            screen[r][c] = '#'


def rotate_row(row: int, shift: int) -> None:
    shift %= 50
    screen[row] = screen[row][-shift:] + screen[row][:-shift]


def rotate_col(col: int, shift: int) -> None:
    shift %= 6
    column = [screen[i][col] for i in range(6)]
    column = column[-shift:] + column[:-shift]
    for i in range(6):
        screen[i][col] = column[i]


def solve_part_1(screen):
    lit_pixels = 0
    for line in screen:
        for pixel in line:
            if pixel == '#':
                lit_pixels += 1
    print(lit_pixels)


def solve_part_2(screen):
    for line in screen:
        print(''.join(line))


if __name__ == '__main__':


    data = open(0).read().splitlines()

    screen = [['.' for _ in range(50)] for _ in range(6)]

    for line in data:
        if 'rect' in line:
            r, c = map(int, line.split(' ')[1].split('x'))
            turn_on_rect(c, r)
        if 'rotate column' in line:
            x, d = map(int, line.split('=')[1].split(' by '))
            rotate_col(x, d)
        if 'rotate row' in line:
            y, d = map(int, line.split('=')[1].split(' by '))
            rotate_row(y, d)



    solve_part_1(screen) 
    solve_part_2(screen)
    
   