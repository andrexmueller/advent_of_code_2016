# Day 3: Squares With Three Sides



def solve_part_1(data):
    triangles_count = 0
    for s in data:
        a, b, c = sorted(s)
        if a + b > c:
            triangles_count += 1
    print(triangles_count)
    

def solve_part_2(data):
    data = list(zip(*data))
    triangles_count = 0
    for line in data:
        for i in range(0, len(line), 3):
            a, b, c = sorted([line[i], line[i+1], line[i+2]])
            if a + b > c:
                triangles_count += 1
    print(triangles_count)


if __name__ == '__main__':

    data = open(0).read().splitlines()
    data = [list(map(int, line.strip().split())) for line in data]
    
    #solve_part_1(data)
    solve_part_2(data)