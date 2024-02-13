# Day 9: Explosives in Cyberspace
import re
import sys

def solve_part_1(data: str) -> None:
    cursor = 0
    decompressed = len(data)
    while True:
        marker = re.search(r'\(\d+x\d+\)', data[cursor:])
        if marker is None:
            break
        pi, pf = marker.span()
        subseq, reps = map(int,data[cursor+pi+1:cursor+pf-1].split('x'))
        decompressed += subseq * (reps - 1) - pf + pi
        cursor += pf + subseq
    print(decompressed)


def solve_part_2(data: str) -> None:
    
    def rec(data: str) -> int:
        cursor = 0
        decompressed = 0
        while True:
            marker = re.search(r'\(\d+x\d+\)', data[cursor:])
            if marker is None:
                break
            pi, pf = marker.span()
            subseq, reps = map(int,data[cursor+pi+1:cursor+pf-1].split('x'))
            decompressed += len(data[cursor:cursor+pi]) + rec(data[pf+cursor:pf+cursor+subseq]) * reps
            cursor += pf + subseq
        return decompressed + len(data[cursor:])

    print(rec(data))

    




if __name__ == '__main__':

    data = open(0).read()
    solve_part_1(data)
    solve_part_2(data)
    

