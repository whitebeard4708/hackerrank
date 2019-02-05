#!/bin/python3

import math
import os
import random
import re
import sys

def check_email(email):
    pattern = "[a-z.]+(@gmail\\.com)$"
    return re.match(pattern, email)

if __name__ == '__main__':
    N = int(input())
    proper_name = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if check_email(emailID):
            proper_name.append(firstName)
    proper_name.sort()
    for name in proper_name:
        print(name) 
