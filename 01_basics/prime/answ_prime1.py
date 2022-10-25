#!/usr/bin/env python3

def all_prime(numb):
    if numb == 1:
        return True
    for i in range(2, numb):
        if numb % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input('Введите n: '))
    print(f'Число {n} {"" if all_prime(n) else "не "}является простым')