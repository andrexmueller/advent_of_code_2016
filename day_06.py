# Day 6: Signals and Noise

from collections import Counter

def solve_part_1(data):
    # transpose data
    data_t = list(zip(*data))
    msg  = ""
    for line in data_t:
        msg += sorted([(v, k) for k, v in Counter(line).items()])[-1][1]
    print(msg)

def solve_part_2(data):
    # transpose data
    data_t = list(zip(*data))
    msg  = ""
    for line in data_t:
        msg += sorted([(v, k) for k, v in Counter(line).items()])[0][1]
    print(msg)



if __name__ == '__main__':


    data = open(0).read().splitlines()
    solve_part_1(data)
    solve_part_2(data)
