#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #
    def lcm(x,y):
        x1 = min(x,y)
        y1 = max(x,y)
        while x1 != 0:
            x1,y1 = y1%x1, x1
        return y1
    def gcd(x,y):
        return x*y//(lcm(x,y))
    def lcm_array(arr):
        while len(arr) >= 2:
            add_ele = lcm(arr[0], arr[1])
            arr = [add_ele]+ arr[2:]
        return arr[0]
    def gcd_array(arr2):
        while len(arr2) >= 2:
            add_ele2 = gcd(arr2[0], arr2[1])
            arr2 = [add_ele2] + arr2[2:]
        return arr2[0]

    lower = gcd_array(a)
    upper = lcm_array(b)
    def count_divide(c, d):
        total_count = d//c
        return len([x for x in range(1,total_count+1) if total_count%x == 0])
    return count_divide(lower, upper) if upper % lower == 0 else 0
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
