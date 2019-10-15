# Birthday Cake Candles
import math
import os
import random
import re
import sys


def birthdayCakeCandles(ar):
    counter = 0
    max_height = max(ar)  # take max value from array
    for i in ar:
        if i == max_height:  # check how many there are max_height
            counter += 1
    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
