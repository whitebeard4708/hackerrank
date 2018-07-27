#!/bin/python3

import sys

def countsum(x):

    def subsum(x,y):
        amount = (x-1)//y
        return y*amount*(amount+1)//2
    return subsum(x,3) + subsum(x,5) - subsum(x,15)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print (countsum(n))
