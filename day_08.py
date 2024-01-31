# Day 8: Two-Factor Authentication


def turn_on_rect(rows: int, cols: int) -> None:
    for r in range(rows):
        for c in range(cols):
            screen[r][c] = '#'


def rotate_row(row: int, shift: int) -> None:
    screen[row] = screen[row][-shift:] + screen[row][:-shift]


def rotate_col(col: int, shift: int) -> None:
    pass


if __name__ == '__main__':


    data = open(0).read().splitlines()

    screen = [tuple('.' for _ in range(50)) for _ in range(6)]

    for line in data:
        if 'rect' in line:
            r, c = map(int, line.split(' ')[1].split('x'))
        if 'rotate column' in line:
            x, d = map(int, line.split('=')[1].split(' by '))
        if 'rotate row' in line:
            y, d = map(int, line.split('=')[1].split(' by '))
            print(line, '*', y+d)

    
    for line in screen:
        print(line)