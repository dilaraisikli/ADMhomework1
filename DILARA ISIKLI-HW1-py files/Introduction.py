#Introduction

#Problem1: Say "Hello, World!" With Python
if __name__ == '__main__':
    print "Hello, World!"

#Problem2: Python If-Else
#check n for it is odd or even and range of the n because of deciding print werid or not werid
#!/bin/python
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(raw_input().strip())
    if (n % 2 == 1):
        print("Weird")
    elif (n % 2 == 0 and n <5 and n>=2):
        print("Not Weird")
    elif (n % 2 ==0 and n<=20 and n>=6):
        print("Weird")
    elif(n % 2 ==0 and n >20):
        print("Not Weird")
#Problem3: Arithmetic Operators
if __name__ == '__main__': #take 2 input than use arithmetic oper.
    a = int(raw_input())
    b = int(raw_input())
    print( a + b)
    print(a-b)
    print(a*b)
#Problem4 : Python Division
from __future__ import division
# take two integers and print integer division and float division,
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(int(a/b))
    print(float(a/b))

#Problem5: Loops
# take n integer. Print n time value * 2
if __name__ == '__main__':
    n = int(raw_input())
    for value in range(n):
        print(value ** 2)

#Problem6: Write a function
# if year can be divided by 4, is a leap year. İf year can be divided by 100, it is NOT a leap year.             #if year  is divisible by 400, it is a leap year.

def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    return leap

#Problem7: Print Function
# read an integer (value) , print 1,2,3..Value
from __future__ import print_function
if __name__ == '__main__':
    value = int(raw_input())

for value in range(1,value+1):
    print(value, end='')
