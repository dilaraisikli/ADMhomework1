# Data types

# Problem1: List Comprehensions

# x,y,z are dimensions of a cuboid along. print a list of all possible coordinates
# i+j+k not equal to n
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
value = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(value)
# Problem2: Find the Runner-Up Score!

# n is list leng. , take n scores and find runner-up (second) print runnerup score
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    maxArr = max(arr)
    runnerUp = -101  # i >=-100 so we can take runnerup=-101 as a first value
    for value in range(n):
        if arr[value] != maxArr and arr[value] > runnerUp:
            runnerUp = arr[value]
    print(runnerUp)

# Problem3: Nested Lists

# Take names and grades for each student. Store them in a nested list.                                                                                        #Print the names of any students  having the second lowest grade.
if __name__ == '__main__':
    nameList = []
    scoreList = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        nameList.append(name)
        scoreList.append(score)

    nestedList = []
    nestedList.extend([list(a) for a in zip(nameList, scoreList)])
    newList = []
    scoreList2 = sorted(scoreList)
    scoreList3 = []
for i in range(len(scoreList2) - 1):
    if (scoreList2[i] < scoreList2[i + 1]):
        scoreList3.append(scoreList2[i])
if (len(scoreList3) == 1 or len(scoreList3) == 0):
    scoreList3.append(scoreList2[-1])
for i in range(len(nestedList)):
    if (nestedList[i][1] == scoreList3[1]):
        newList.append(nestedList[i][0])

for i in sorted(newList):
    print
    i
    # Problem4: Finding the percentage

# take n students for names and marks of lessons. Required to save the record in a dictionary data type.
# Output the average percentage marks obtained by that student, correct to two decimal places
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

    for key, value in student_marks.items():
        if (query_name == key):
            print
            "%.2f" % (sum(value) / len(value))

# Problem5: Lists
# The first line contains an integer,n , denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands described above.
if __name__ == '__main__':
    N = int(raw_input())
    list = []
    for i in range(N):
        value = raw_input().split()
        if len(value) == 3:
            eval("list." + value[0] + "(" + value[1] + "," + value[2] + ")")
        elif len(value) == 2:
            eval("list." + value[0] + "(" + value[1] + ")")
        elif value[0] == "print":
            print
            list
        else:
            eval("list." + value[0] + "()")
# Problem6: Tuples
# take n integers, create a tüple of integers. Then compute and print the hash() of tuple
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    print
    hash(t)

