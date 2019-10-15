# Built-ins
# Problem1: Zipped!
NX = map(int, raw_input().split())  # take number of students and number of lessons
Marks = [map(float, raw_input().split()) for _ in range(NX[1])]  # take marks of students
for i in zip(*Marks):  # zip marks of same lessons and aver. them print aver.

    print
    sum(i) / NX[1]

# Problem2: Athlete Sort!
from operator import itemgetter

N, M = [int(x) for x in raw_input().strip().split()]  # take number of atheletes and number of attributes
L = [0] * N
for i in xrange(N):
    L[i] = [int(x) for x in raw_input().strip().split()]
K = int(raw_input())  # index of selected athelets
L.sort(key=itemgetter(K))  # sort list according to K
for A in L:
    print
    ' '.join(map(str, A))

# Problem3: GinortS
from string import ascii_lowercase, ascii_uppercase

sortRule = ascii_lowercase + ascii_uppercase + "1357902468"  # create a sort rule first all lowercaes second uppercases third odd numbers and last one even numbers
unsorted = raw_input()  # take a string

print
reduce(lambda x, y: x + y, sorted(unsorted, key=sortRule.index))  # use reduce fun. to sorted

