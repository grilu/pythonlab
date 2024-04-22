#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    
    positive = 0
    negative = 0
    zeros = 0
    
    n = len(arr)
    
    
    
    for i in range(n):
        print(i)
        if arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += 1
        else:
            zeros += 1
    
    #print(positive)
    #print(negative)
    #print(zeros)
    
    pos = positive/n
    neg = negative/n
    zer = zeros/n 
    
    print(format(pos, '.6f'))    
    print(format(neg, '.6f'))
    print(format(zer, '.6f'))     
            
            

if __name__ == '__main__':
    
    arr = (-4, 3, -9, 0, 4, 1)


    plusMinus(arr)
