#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    ln = len(arr)
    answer = [ln]
    arr.sort()
    counter = 1
    while arr:
        curr_al = arr.pop(0)
        while arr and arr[0] == curr_al:
            arr.pop(0)
            counter += 1
        ln -= counter
        counter = 1
        answer.append(ln)
    return answer[:-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()