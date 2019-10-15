# Collections
# Problem1: collections.Counter()
# Have a list containing the size of each shoe.
# There are numbers of customers who are willing to pay price only if they get the shoe of their desired size
# when a shose is sold , remove the shose number and cont. add price of solded shose
numOfSho = input()
shoeSizes = list(map(int, raw_input().split()))
numOfCus = input()
total = []
money = []
for i in range(numOfCus):
    cusAndPrice = list(map(int, raw_input().split()))
    total.append(cusAndPrice)

for value in total:

    if value[0] in shoeSizes:
        money.append(value[1])
        shoeSizes.remove(value[0])

print
sum(money)

# Problem2: Collections.namedtuple()
# print the average marks of the list corrected to 2 decimal places.
from collections import namedtuple

n = input()  # take student numbers
students = namedtuple('students', raw_input().split())  # create a tuple as students
print("%.2f" % (sum([float(i.MARKS) for i in
                     [students(*raw_input().split()) for j in range(n)]]) / n))  # sum marks and div them to get aver.

# Problem3: Collections.OrderedDict()
# list of  items together with their prices that consumers bought on a particular day. #print each item_name and net_price in order of its first occurrence.
from collections import OrderedDict

dic = OrderedDict()
n = int(raw_input())
for _ in range(n):
    l = raw_input().split()
    item = ' '.join(l[:-1])
    price = int(l[-1])
    if item in dic:  # item in dic or not ?
        dic[item] += price
    else:
        dic[item] = price  # if not item = price
for key in dic:
    print('{} {}'.format(key, dic[key]))

# Problem4: Word Order
# output order should correspond with the input order of appearance of the word
from collections import OrderedDict

n = int(input())

dic = OrderedDict()
for _ in range(n):
    nextWord = raw_input()
    if nextWord in dic:
        dic[nextWord] = dic[nextWord] + 1
    else:
        dic[nextWord] = 1

print(len(dic.values()))  # output the number of distinct words from the input.
result = (dic.values())
print
' '.join(map(str,
             result))  # output the number of occurrences for each distinct word according to their appearance in the input.

# Problem5: Collections.deque()
# Perform append, pop, popleft and appendleft methods on an empty deque (d) and print the result
from collections import deque

d = deque()
n = input()

for i in xrange(n):
    methodsAndValues = raw_input().split()
    if methodsAndValues[0] == 'append':
        d.append(int(methodsAndValues[1]))

    if methodsAndValues[0] == 'appendleft':
        d.appendleft(int(methodsAndValues[1]))
    if methodsAndValues[0] == 'pop':
        d.pop()
    if methodsAndValues[0] == 'popleft':
        d.popleft()

print
' '.join(map(str, d))

# Problem6: Company Logo
# Print the three most common characters along with their occurrence count each on a separate line.Sort output in descending order of occurrence count. If the occurrence count is the same, sort the characters in alphabetical order.
from operator import itemgetter

k = raw_input()
list1 = list(k)
list2 = list1  # copy list to compare them
a = set(list2)  # create a set for remove duplication
c = list(a)  # create a list again for sorted
b = sorted(c)
maxx = []
sortedL = []
for i in range(len(b)):
    count = 0
    for j in range(len(list2)):

        if (b[i] == list2[j]):
            count = count + 1
    maxx.append(count)

y = zip(b, maxx)  # union 2 lists

mlll = sorted(y, key=itemgetter(1), reverse=True)

for i in range(3):
    sortedL.append(mlll[i])

for x in sortedL:
    print(x[0] + " " + str(x[1]))

# Problem7: DefaultDict Tutorial
# For each  words, check whether the word has appeared in group A or not. Print the indices of each occurrence of M in group A . If it does not appear, print -1.
NM = raw_input().split()
N = int(NM[0])
M = int(NM[1])
A = []
B = []
for i in range(N):
    A.append(raw_input())
for i in range(M):
    B.append((raw_input()))
indice = []
for i in range(M):
    indice.append([])
    for j in range(N):  # Print the indices of each occurrence of M in group A
        if B[i] == A[j]:
            indice[i].append(str(j + 1))
    if len(indice[i]) == 0:  # If it does not appear, print -1.
        indice[i].append('-1')
for i in range(len(indice)):
    print(' '.join(indice[i]))

# Problem8: Filling Up!

# The first line contains a single integer , the number of test cases.
# For each test case, there are  lines.
# The first line of each test case contains , the number of cubes.
# The second line contains  space separated integers, denoting the sideLengths of each cube in that order.
x = int(input())
for i in range(0, x):
    y = int(input())
    L = list(map(int, raw_input().split()))
    while len(L) >= 2:
        k = len(L)
        if (L[k - 1] >= L[k - 2]):
            L.pop(k - 1)

        elif (L[0] >= L[1]):
            L.pop(0)

        else:
            break

    if len(L) <= 2:
        print("Yes")
    else:
        print("No")
