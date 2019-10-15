#Recursive Digit Sum
#It must return the calculated super digit as an integer.
#superDigit has the following parameter(s):
#n: a string representation of an integer
#k: an integer, the times to concatenate n to k make

import math
import os
import random
import re
import sys

def digDivten(num):

    if num/10 == 0:
        return num
    else:
        return digDivten(sum(list(map(int, list(str(num))))))

def superDigit(n, k):
    a = digDivten(sum(list(map(int, list(str(n)))))*k)
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

