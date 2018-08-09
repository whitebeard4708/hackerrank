#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    ans = []
    for grade in grades:
        if grade < 38: ans.append(grade)
        else:
            if grade - (grade//5)*5 < 3: ans.append(grade)
            else: ans.append(((grade//5)+1)*5)
    return ans

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()