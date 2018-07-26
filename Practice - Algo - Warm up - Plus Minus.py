#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count1 = len([x for x in arr if x > 0])/len(arr)
    count2 = len([x for x in arr if x < 0])/len(arr)
    count3 = len([x for x in arr if x == 0])/len(arr)
    print('%.6f' %count1)
    print('%.6f' %count2)
    print('%.6f' %count3)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
