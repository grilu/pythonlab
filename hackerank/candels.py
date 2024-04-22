#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    
    top = max(candles)
    result = []
    
    for i in (candles):
        if top == i:
            result.append(i)
            
    print(result)

if __name__ == '__main__':
    
    candles = (3, 2, 1, 4)

    result = birthdayCakeCandles(candles)


