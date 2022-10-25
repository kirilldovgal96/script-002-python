#!/usr/bin/env python3

a = (input('Введите координату X '))
b = (input('Введите координату Y '))
c = (input('Введите координату Z '))
d = (input('Введите Значение City '))
mesto = (a, b, c, d)
out = (mesto[3].lower(), mesto[0], mesto[2])
print(f'{out}')
