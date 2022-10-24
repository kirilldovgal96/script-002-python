#!/usr/bin/env python3
import math

fcatet = int(input('Введите длину первого катета: '))
tcatet = int(input('Введите длину второго катета: '))
def hypo(fcatet, tcatet):
    return math.sqrt(fcatet**2  + tcatet**2)
dlina=hypo(fcatet, tcatet)
print(f'Длина гипотенузы {dlina:.2f}')