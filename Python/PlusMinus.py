#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    arr.sort()
    start_0 = bisect.bisect_left(arr, 0)
    end_0 = bisect.bisect_right(arr, 0)

    print("%.6f" % round((len(arr)-end_0)/len(arr), 6))
    print("%.6f" % round(start_0/len(arr), 6))
    print("%.6f" % round((end_0-start_0)/len(arr), 6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
