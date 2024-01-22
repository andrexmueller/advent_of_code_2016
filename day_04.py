# Day 4: Security Through Obscurity
import re
from string import ascii_lowercase
from collections import Counter


def solve_part_1(data):
    sec_ids_sum = 0
    for line in data:
        name, checksum = re.split(r'-\d+', line)
        name = name.replace('-', '')
        sec_id = int(re.findall(r'\d+', line)[0])
        ordered_counter = sorted(
            [(v, k) for k, v in Counter(name).items()], key= lambda t: (t[0], -ord(t[1])), reverse=True
        )
        five_more_freq = ''.join([t[1] for t in ordered_counter[:5]]) 
        if checksum[1:-1
                    ] == five_more_freq:
            sec_ids_sum += sec_id
        
    print(sec_ids_sum)


def solve_part_2(data):
    LETTERS = 26
    START_ASCII_IDX = 97
    target = "northpole object storage"
    for line in data:
        name, _ = re.split(r'-\d+', line)
        sec_id = int(re.findall(r'\d+', line)[0])
        shifted = ''.join([chr((ord(c)- START_ASCII_IDX + sec_id) % LETTERS + START_ASCII_IDX) for c in ascii_lowercase])
        table = name.maketrans(ascii_lowercase+'-', shifted+' ')
        decoded = name.translate(table)
        if decoded == target:
            print(sec_id)


if __name__ == '__main__':

    data = open(0).read().splitlines()
    

    solve_part_1(data)
    solve_part_2(data)

