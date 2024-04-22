import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    # Write your code here
    Alice = 0
    Bob  =0
    
    for i in range(3):
        if a[i] > b[i]:
            Alice += 1
        elif a[i] < b[i]:
            Bob += 1
            
    return [Alice, Bob]
            
        
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
