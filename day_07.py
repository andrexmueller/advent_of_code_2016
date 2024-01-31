# Day 7: Internet Protocol Version 7

import re


def search_abba(s: str) -> bool:
    for i in range(len(s)-3):
        if s[i:i+2] == s[i+2:i+4][::-1] and s[i] != s[i+1]:
            return True
    return False


def search_bab(s: str) -> set:
    babs = set()
    for i in range(len(s)-2):
        if s[i] == s[i+2] and s[i] != s[i+1]:
            babs.add(s[i:i+3])
    return babs


def solve_part_1(data):
    tsl = 0
    for line in data:
        outbracks = re.split(r'\[[a-z]+\]', line)
        inbracks = re.findall(r'\[[a-z]+\]', line)
        invalid = False
        counter = False
        for ib in inbracks:
            if search_abba(ib):
                invalid = True
        if invalid:
            continue
        for ob in outbracks:
            if search_abba(ob):
                counter = True
        if counter:
            tsl += 1
    print(tsl)


def solve_part_2(data):
    ssl = 0
    for line in data:
        outbracks = re.split(r'\[[a-z]+\]', line)
        inbracks = re.findall(r'\[[a-z]+\]', line)
        
        babs = set()
        for ib in inbracks:
            babs |= search_bab(ib)

        abas = set()
        for ob in outbracks:
            abas |= search_bab(ob)

        for bab in babs:
            aba = bab[1] + bab[0] + bab[1]
            if aba in abas:
                ssl += 1
                break
    
    print(ssl)





if __name__ == '__main__':

    data = open(0).read().splitlines()
    
    solve_part_1(data)
    solve_part_2(data)