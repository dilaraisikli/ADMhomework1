# Numpy

# Problem1: Arrays
import numpy


def arrays(arr):
    NumArr = arr[::-1]
    return numpy.array(NumArr, float)  # it starts from the end, towards the first, taking each element. So it reverses


arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)


def arrays(arr):
    NumArr = arr[::-1]
    return numpy.array(NumArr, float)


# Problem2: Shape and Reshape
# change the dimensions of an array.
import numpy

print
numpy.reshape(map(int, raw_input().split()), (3, 3))  # print 3X3 NumPy array.

# Problem3: Transpose and Flatten
import numpy

N, M = map(int, raw_input().split(' '))  # number of row and columns
arr = []
for n in range(N):
    arr.append(map(int, raw_input().split()))  # put element into array
NumArry = numpy.array(arr)

print
numpy.transpose(arr)  # create transpose for array
print
NumArry.flatten()  # create flatten for numpy array

# Problem4: Concatenate

import numpy

N, M, P = map(int, raw_input().strip().split(' '))  # n and m are row p is colu.
arr1 = numpy.empty([N, P], dtype='int')  # Create an array for first array
arr2 = numpy.empty([M, P], dtype='int')  # Create an array for second array
NumofTotal = len(arr1) + len(arr2)
for i in range(NumofTotal):
    if i < len(arr1):
        arr1[i] = numpy.array(map(int, raw_input().split(' ')))  # put element into arr1 until end of len. arr1
    else:
        arr2[i - N] = numpy.array(map(int, raw_input().split(' ')))  # put element into arr2

print
numpy.concatenate((arr1, arr2), axis=0)  # concatenate arrays

# Problem5: Zeros and Ones
# print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.
import numpy

N = map(int, raw_input().split())  # space-separated integers row colum. and iteate time
print
numpy.zeros(N, dtype='int_')  # print zeros
print
numpy.ones(N, dtype='int_')  # print ones

# Problem6: Eye and Identity

# print an array of size nXm with its main diagonal elements as 1's and 0's everywhere else
import numpy

N, M = map(int, raw_input().split())

a = str(numpy.eye(N, M, k=0)).replace("0", " 0")

b = a.replace("1", " 1")
print
b

# Problem7: Array Mathematics
# Print the result of each operation
import numpy

n = int(raw_input().split(' ')[0])


def makeArray(n):
    arr = []
    for j in range(n):
        arr.append(raw_input().split(' '))
    return arr


A = numpy.array(makeArray(n), int)
B = numpy.array(makeArray(n), int)

print
numpy.add(A, B)  # + numpy
print
numpy.subtract(A, B)  # - mod pow
print
numpy.multiply(A, B)  # * numpy
print
numpy.divide(A, B)  # / numpy
print
numpy.mod(A, B)  # mod numpy
print
numpy.power(A, B)  # pow numpy

# Problem8: Floor, Ceil and Rint

import numpy as np

A = np.array(map(float, raw_input().split()))
print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))

# Problem9: Sum and Prod
import numpy

N, M = map(int, raw_input().split())
Arr = numpy.array([map(int, raw_input().split()) for i in range(N)])  # take array and turn this as numpy array

sumOfArr = numpy.sum(Arr, axis=0)  # calculate sum of arr
print
numpy.prod(sumOfArr)  # prod of sum of arr

# Problem10: Min and Max
# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy

N, M = map(int, raw_input().split())  # take number of dimensions

arr = numpy.array([raw_input().split() for i in range(N)], int)

print
numpy.max(numpy.min(arr, axis=1))  # take min of max of arr.numpy

# Problem11: Mean, Var, and Std
# The mean along axis 1
# The var along axis 0
# The std along axis none

import numpy

n, m = map(int, raw_input().split())
arr = numpy.array([map(int, raw_input().split()) for i in range(n)])
print
numpy.mean(arr, axis=1)
print
numpy.var(arr, axis=0)
print
numpy.around(numpy.std(arr), 12)

# Problem12: Dot and Cross
import numpy

N = int(raw_input())
A = numpy.array([map(int, raw_input().split()) for i in range(N)])  # take first array
B = numpy.array([map(int, raw_input().split()) for i in range(N)])  # take second array

print
numpy.dot(A, B)  # compute their matrix product.

# Problem13: Inner and Outer
# compute A's and B's inner and outer product.

import numpy

a = list(map(int, raw_input().split()))
b = list(map(int, raw_input().split()))

a = numpy.array(a)
b = numpy.array(b)

print(numpy.inner(a, b))
print(numpy.outer(a, b))

# Problem14: Polynomials
#  task is to find the value of P at point X.
import numpy

coefficients = raw_input().split()
coefficient = map(float, coeff)
x = float(raw_input())
print
numpy.polyval(coeff, x)

# Problem15: Linear Algebra
# find the determinant of matrix A
import numpy as np

N = input()
A = np.array([list(map(float, raw_input().split())) for _ in range(N)])
print(float(numpy.linalg.det(A)))

