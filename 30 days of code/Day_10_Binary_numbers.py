#!/bin/python3

import math
import os
import random
import re
import sys

def max_consecutive1(n):
    binary = bin(n)[2:]
    ans = 0
    count = 0
    for char in binary:
        if char == "1":
            count += 1
            ans = max(count, ans)
        else:
            count = 0
    return ans

if __name__ == '__main__':
    n = int(input())
    print(max_consecutive1(n))
