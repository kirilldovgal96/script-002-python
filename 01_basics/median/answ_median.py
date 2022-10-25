#!/usr/bin/env python3
def median(*nomer):
    nom=len(nomer)
    if nom==0:
        return 0
    if nom%2==0:
        return (nomer[(nom-1)//2]+nomer[nom//2])/2
    return nomer[nom//2]

print(median())
print(median(1, 2, 6))
print(median(1, 2, 6, 19))

