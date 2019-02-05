#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

swaps = 0

for i in range(n-2, -1, -1):
    start = 0
    while start <= i:
        if a[start] > a[start+1]:
            a[start], a[start+1] = a[start+1], a[start]
            swaps += 1
            
        start += 1

print("Array is sorted in {} swaps.".format(swaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))


