#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n,arr):
    # Write your code here
    tmp = arr.pop()
    arr.append(arr[-1])
    
    for i in range(len(arr)-2, -1, -1):
        if (i+1) < len(arr):
            if (i+1) < len(arr) and tmp < arr[i]:
                arr[i+1] = arr[i]
                if i == 0:
                    arr[i] = tmp
                for j in arr:
                    print(j, end=" ")
            else: 
                arr[i+1] = tmp
                for j in arr:
                    print(j, end=" ")
                break
        print(end="\n")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
