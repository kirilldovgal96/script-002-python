#!/usr/bin/env python3
a=(input('Введите первое число: '))
b=0 
summa=0
while a:
    kol=int(a)
    summa+=kol
    b+=1
    a=(input('Введите следующее число: '))
if (a!=''):
    print (f'Среднее всех чисел: {summa/kol}')
else:
    print(f'Error 0')