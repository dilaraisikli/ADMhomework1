# Sets

# Problem1: Introduction to Sets
# take array, turn to set, sum set and divide sum of set by len(set)
def average(array):
    # your code goes here
    total = 0

    for i in range(len(array)):
        total = total + array[i]
        i += 1

    av = total / (len(array))
    sett = set(array)
    sums = sum(sett)
    lenn = len(sett)
    avv = sums / lenn
    return avv
    if __name__ == '__main__':
        n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print
    result


# Problem2: No Idea!
# A and B are   disjoint sets, if a integer is in A happiness +1 else if integer is in b happiness -1
mANDn = set(map(int, raw_input().split()))
arrays = (map(int, raw_input().split()))
A = set(map(int, raw_input().split()))
B = set(map(int, raw_input().split()))
result = 0

for i in arrays:
    if i in A:
        result = result + 1
    if i in B:
        result = result - 1
print
result

# Problem3: Symmetric Difference
# take two string and compare them. Select symmetric difference elements and print it
if __name__ == '__main__':

    int(raw_input())
    n = raw_input().split()  # first string len
    ni = set(list(map(int, n)))  # convert from string to set

    int(raw_input())
    m = raw_input().split()  # second string len
    mi = set(list(map(int, m)))  # convert from string to set

    reslist = []  # create new list for add diffrences

    for i in list(ni.difference(mi)):
        reslist.append(i)
    for j in list(mi.difference(ni)):
        reslist.append(j)
    for k in sorted(reslist):
        print
        k

# Problem4: Set .add()
# create a set to remove duplicate elements from the list and check len of the set
value = int(raw_input())
valueOfset = set()

for i in range(value):
    string = str(raw_input())
    valueOfset.add(string)

print
len(valueOfset)

# Problem5: Set .union() Operation
# take to set and compare them for find union elements. Print number of union elements
NUMBEROFVALUE1 = input()
value1 = set(map(int, raw_input().split()))
NUMBEROFVALUE2 = input()
value2 = set(map(int, raw_input().split()))
a = value1.union(value2)
b = len(a)
print
b

# Problem6: Set .intersection() Operation
# take to set and compare them for find intersection elements. Print number of intersection element
EnglishNewspaper = input()
studentsE = set(map(int, raw_input().split()))
Frenchnewspaper = input()
studentsF = set(map(int, raw_input().split()))

SETT = studentsE.intersection(studentsF)
print
len(SETT)

# Problem7: Set .difference() Operation
# find total number of students who are subscribed to the English newspaper only.
EnglishNewspaper = input()
studentsE = set(map(int, raw_input().split()))
Frenchnewspaper = input()
studentsF = set(map(int, raw_input().split()))

SETT = studentsE.difference(studentsF)  # select only english new. subscribed
print
len(SETT)

# Problem8: Set .symmetric_difference() Operation
# a union b – (a and b)
EnglishNewspaper = input()
studentsE = set(map(int, raw_input().split()))
Frenchnewspaper = input()
studentsF = set(map(int, raw_input().split()))

SETT = studentsE.symmetric_difference(studentsF)
print
len(SETT)

# Problem9: Set Mutations
# Take operation name and implement(update) them
numberOfElements = input()
listOfelements = set(map(int, raw_input().split()))
numberOfotherSets = input()
for i in range(numberOfotherSets):
    kind = raw_input().split()
    otherset = set(map(int, raw_input().split()))

    if kind[0] == 'intersection_update':
        listOfelements.intersection_update(otherset)
    if kind[0] == 'update':
        listOfelements.update(otherset)
    if kind[0] == 'symmetric_difference_update':
        listOfelements.symmetric_difference_update(otherset)
    if kind[0] == 'difference_update':
        listOfelements.difference_update(otherset)

print
sum(listOfelements)

# Problem10: Check Subset
# check subset if If set A is subset of set B, print True else False
testCases = input()
listOfDes = []
for i in range(testCases):
    elemOfA = input()
    A = set(map(int, raw_input().split()))
    elemOfB = input()
    B = set(map(int, raw_input().split()))
    if (B.issuperset(A) == False):  # is super set or not?
        listOfDes.append(False)
    if (B.issuperset(A) == True):  # is super set or not?
        listOfDes.append(True)

for value in listOfDes:
    print
    value

# Problem11: Check Strict Superset
# print True if set A is a strict superset of all other sets. Otherwise, print False.
elements = set(map(int, raw_input().split()))
otherSetsNum = input()
listOfDes = []

for i in range(otherSetsNum):
    otherSet = set(map(int, raw_input().split()))
    if (elements.issuperset(otherSet) == False):  # is super set or not?
        listOfDes.append(False)
    if (elements.issuperset(otherSet) == True):  # is super set or not?
        listOfDes.append(True)
print(all(listOfDes))

# Problem12: The Captain's Room
from collections import Counter

K = int(raw_input())  # size of each group.
RoommNumList = raw_input().split()  # unordered elements of the room number list

RoommNumList = Counter(RoommNumList)
print[x
for x in RoommNumList.keys() if RoommNumList[x] == 1][0]
