#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):

    # Write your code here.
    if s[-2:] == "AM": return s[:-2]
    else:
        newhour = str(int(s[:2]) + 12)
        return newhour + s[2:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
