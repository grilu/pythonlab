#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    
    a = min(arr)
    b = max(arr)
    
    amin = []
    bmax = []
    n = len(arr)
    
    for i in (arr):
        if a != i:
            bmax.append(i)
            
   
    for i in (arr):
        if b != i:
            amin.append(i)
            
    print(sum(amin), sum(bmax))
    
    

if __name__ == '__main__':

    #arr = list(map(int, input().rstrip().split()))
    
    arr = (1, 1, 2, 3, 4)

    miniMaxSum(arr)
