# Strings
# Problem1: sWAP cASE
# convert all lowercase letters to uppercase letters and vice versa.
def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print
    result


# Problem2: String Split and Join
# given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
def split_and_join(line):
    string = line
    sp = string.split(" ")
    return "-".join(sp)
    if __name__ == '__main__':
        line = raw_input()
    result = split_and_join(line)  # use function
    print
    result


# Problem3: What’s your name?
# take the firstname and lastname.
# Print:Hello firstname lastname! You justdelved into python.
def print_full_name(a, b):
    print("Hello " + a + " " + b + "! You just delved into python.")


# Problem4: Mutations
# Take a string.
# position : index location
# character is which
def mutate_string(string, position, character):
    string = string[:(position)] + character + string[(position + 1):]  # replace the character at index
    return (string)


if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print
    s_new


# Problem5: Find a string
def count_substring(string, subString):
    # take string and substring to check string include substring or not
    count = 0

    for i in range(len(string)):
        if subString[0] == string[i]:  # if string has first letter of subst. continu.
            if subString == string[i:i + len(subString)]:  # if string has all letter of sub. add 1 to count
                count += 1
    return (count)


if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()

    count = count_substring(string, sub_string)
    print
    count
# Problem6: String Validators
# check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
if __name__ == '__main__':
    string = raw_input()

print
any(value.isalnum() for value in string)  # print True if has any alphanumeric characters
print
any(value.isalpha() for value in string)  # print True if  has any alphabetical characters.
print
any(value.isdigit() for value in string)  # print True if  has any digits
print
any(value.islower() for value in string)  # print True if  has any lowercase characters
print
any(value.isupper() for value in string)  # , print True if  has any uppercase characters

# Problem7: Tex Alignment

fre = int(input())
h = 'H'
for i in range(fre):
    print((h * i).rjust(fre - 1) + h + (h * i).ljust(fre - 1))

for i in range(fre + 1):
    print((h * fre).center(fre * 2) + (h * fre).center(fre * 6))

for i in range((fre + 1) // 2):
    print((h * fre * 5).center(fre * 6))

for i in range(fre + 1):
    print((h * fre).center(fre * 2) + (h * fre).center(fre * 6))

for i in range(fre):
    print(((h * (fre - i - 1)).rjust(fre) + h + (h * (fre - i - 1)).ljust(fre)).rjust(fre * 6))


# Problem8: Text Wrap
# wrap the string into a paragraph of width
def wrap(string, max_width):
    text = textwrap.fill(string, max_width)  # sperate string to substring which has width is max_width
    return text


if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print
    result


# Problem9: Designer Door Mat

# Mat size must be n*m. Have 'WELCOME' written in the center.
# should only use |, . and - characters.
def door():
    n, m = map(int, raw_input().split())
    welM = (m - 7) / 2
    first = "-"
    second = ".|."
    wel = "WELCOME"
    width = 6
    for i in range((n - 1) / 2):  # first part of design
        print(
            (first * ((m - (3 * (2 * i + 1))) / 2)) + (second * (2 * i + 1)) + (first * ((m - (3 * (2 * i + 1))) / 2)))
    print((first * welM) + wel + (first * welM))  # center of design
    for i in xrange(n - 2, -1, -2):  # last part of design
        print(str('.|.') * i).center(m, '-')


if __name__ == '__main__':
    door()


# Problem10: String Formatting
def print_formatted(number):
    # take number of iterator. Print the following values for each integer from 1 to len(num)
    # 1.Decimal, 2. Octal, 3. Hexadecimal (capitalized), And 4. Binary

    width = len('{:b}'.format(number))
    for i in range((number)):
        formatS = "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format((i + 1), width=width)
        print
        formatS


# Problem11: Capitalize!
#  first and last names of people begin with a capital letter
def solve(s):
    ListS = list(s)
    for i in range(0, len(ListS)):
        if (i == 0):
            ListS[i] = ListS[i].capitalize()  # check first word
        if (ListS[i].isspace()):  # check every word after spaces
            ListS[i + 1] = ListS[i + 1].capitalize()
            i += 1
    newString = "".join(ListS)
    return (newString)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# Problem12: The Minion Game
def minion_game(input_string):
    list1 = list(input_string)
    s = 0
    k = 0
    for i in range(0, len(list1)):
        if list1[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O',
                        'U']:  # if element is vowel it means this subset start with vowel and score is +  len(list1) - (i+1) + 1 and kevin gains tihs score
            k = k + len(list1) - (i + 1) + 1  # artık olan
        else:  # if element is slient letter it means this subset start with vowel and score is +  len(list1) - (i+1) + 1 and draw gains tihs score
            s = s + len(list1) - (i + 1) + 1  # artık
    if k > s:
        print
        "Kevin", k
    elif k == s:
        print
        "Draw"
    else:
        print
        "Stuart", s


if __name__ == '__main__':
    s = raw_input()
    minion_game(s)

# Problem13: Alphabet Rangoli
from collections import defaultdict
import string


def print_rangoli(n):
    width = 4 * (n - 1) + 1
    l = string.ascii_lowercase[:n]

    for i in range(n - 1):
        s = l[n - 1 - i:]
        print(('-'.join(s[-1:0:-1] + s)).center(width, '-'))

    for i in range(n - 1, -1, -1):
        s = l[n - 1 - i:]
        print(('-'.join(s[-1:0:-1] + s)).center(width, '-'))


if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)


# Problem14: Merge the Tools!
def merge_the_tools(string, k):
    for i in range(0, (len(string) - k + 1), k):
        s = list(string[i:i + k])  # divide by k
        print
        ''.join([x for i, x in enumerate(s) if s.index(x) == i])  # non-distinct characters


if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)

