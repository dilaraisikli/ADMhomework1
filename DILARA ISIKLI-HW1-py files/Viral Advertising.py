
#Viral Advertising
n = int(input()) #the integer number of days
count = 0
people = 5 # they advertise it to exactly 5 people on social media

for _ in range(n):
    count = count + people // 2
    people = (people // 2) * 3
print(count)
