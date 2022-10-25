#!/usr/bin/env python3

from answ_prime1 import all_prime

def prime2(num):
    num += 1
    while not all_prime(num):
        num += 1
    return num

if __name__ == '__main__':
    n = int(input('Введите n: '))
    print(
        f'Следующее простое число после {n} это {prime2(n)}')