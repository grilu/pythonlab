#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    unique = 0

    for i in a:
        unique ^= i 
    return unique
       

if __name__ == '__main__':


    a = [1,2,4,3,2,1]

    result = lonelyinteger(a)

    print(result)
