#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):

    # Write your code here.
    if (s[:2] != "12" and s[-2:] == "AM") or (s[:2] == "12" and s[-2:] == "PM"): return s[:-2]
    
    elif (s[:2] == "12" and s[-2:] == "AM"):
        newhour = int(s[:2])-12
        newhour1=  "%02d" %newhour
        return newhour1 + s[2:-2]
    
    else:
        newhour2 = str(int(s[:2]) + 12)
        return newhour2 + s[2:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
