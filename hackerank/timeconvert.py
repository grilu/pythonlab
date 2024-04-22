#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    
    hour = int(s[0:2])
    minute = s[3:5]
    second  = s[6:8]
    period  = s[8:10]
   
    
    if period == 'AM':
        if hour == 12:
            # Convert midnight hour to '00'
            hour = '00'
        else:
            # Keep the hour as it is, but ensure it has two digits
            hour = f"{hour:02}"
    else:  # PM period
        if hour != 12:
            # Convert PM hour to military time by adding 12
            hour = f"{hour + 12:02}"
        else:
            # Keep the noon hour as '12'
            hour = f"{hour:02}" 
    
    print(f"{hour}:{minute}:{second}")

if __name__ == '__main__':
   
    s = '04:01:23PM'

    result = timeConversion(s)


