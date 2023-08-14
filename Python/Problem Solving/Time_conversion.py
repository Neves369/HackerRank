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
    time_parts = s.split(":")
    hour = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2][:2]) 

    if s[-2:] == "PM" and hour != 12:
        hour += 12
    elif s[-2:] == "AM" and hour == 12:
        hour = 0
    
    formatted_time = "{:02d}:{:02d}:{:02d}".format(hour, minutes, seconds)
    return formatted_time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
