# Kangaroo
# Print YES if they can land on the same location at the same time; otherwise, print NO.
x1, v1, x2, v2 = map(int, raw_input().split())  # take  starting position and jump distance for kangaroos

if v1 == v2 or (x1 - x2) % (v2 - v1) != 0 or (x1 - x2) // (v2 - v1) < 0:
    print('NO')
else:
    print('YES')  # meet at the same location after same number of jumps print yes

