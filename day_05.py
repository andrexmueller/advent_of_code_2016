import hashlib



def solve_part_1(data: str) -> None:
    c = 1
    pwd = ''
    while len(pwd) < 8:
        
        string = data + str(c)
        hashed = hashlib.md5(string.encode()).hexdigest()
        if hashed[:5] == '00000':
            pwd += hashed[5]
            print(pwd)
        c += 1

    print(pwd)


def solve_part_2(data: str) -> None:
    c = 1
    pwd = [None for _ in range(8)]
    found = 0
    while found < 8:
        string = data + str(c)
        hashed = hashlib.md5(string.encode()).hexdigest()
        if hashed[:5] == '00000':
            print(hashed, pwd)
            if hashed[5].isdigit() and 0 <= int(hashed[5]) < 8:
                if pwd[int(hashed[5])] is None:
                    pwd[int(hashed[5])] = hashed[6]
                    found += 1
        c += 1

    print(''.join(pwd))


if __name__ == '__main__':
    
    #solve_part_1('wtnhxymk')
    solve_part_2('wtnhxymk')
