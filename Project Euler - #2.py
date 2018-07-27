#!/bin/python3

import sys

def fiboevensum(x):
    a,b, count = 1,1,0
    while b <= x:
        a,b = b, a+b
        if a%2 == 0: count += a
    return count

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print (fiboevensum(n))
