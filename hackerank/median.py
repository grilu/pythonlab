#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    
    a = sorted(arr)
    
    n = len(a)
    
    median = math.floor(n/2)
    
    print(a[median])

if __name__ == '__main__':
    
    arr = [5, 3, 4, 1, 2]
    findMedian(arr)
    