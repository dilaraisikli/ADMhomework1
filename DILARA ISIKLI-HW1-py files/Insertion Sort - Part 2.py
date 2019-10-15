count = arr[i]

while i > 0 and ar[i - 1] > count:
    arr[i] = arr[i - 1]
    i = i - 1;
arr[i] = count;
return arr


def insertionsort(arr, n):
    for i in range(1, n):
        arr = LastOne(n, arr, i);
        print(' '.join(map(str, arr)))


n = int(input())  # an integer representing the length of the array
arr = list(map(int, raw_input().split(" ")))  # take array
insertionsort(arr, n)





