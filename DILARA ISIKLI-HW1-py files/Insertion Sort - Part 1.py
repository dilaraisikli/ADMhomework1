
#Insertion Sort - Part 1
#Print the array as a row of space-separated integers each time there is a shift or insertion.
import sys
count = None
arr = []
for line in sys.stdin:
    if count is None:
        count = int(line.strip()) #size of the array
        continue
    arr = [int(i) for i in line.strip().split(' ')] #array of integers to sort

val = arr[-1]
for i in range(count - 1):
    if val >= arr[count - 2 - i]:
        arr[count - 2 - i + 1] = val
        print(' '.join([str(j) for j in arr]))
        break
    else:
        arr[count - 2 - i + 1] = arr[count - 2 - i]
        print(' '.join([str(j) for j in arr]))

if val not in arr:
    arr[0] = val
    print(' '.join([str(i) for i in arr]))



