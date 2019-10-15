# Regex and Parsing Challenges
# Problem1: Detect Floating Point Number
# a valid float number must satisfy all of the following requirements:
# Number can start with +, - or . symbol.
# Number must contain at least 1 decimal value.
# Number must have exactly one . symbol.
# Number must not give any exceptions when converted using float(N).
import re

n = input()
for _ in range(n):
    print(bool(re.match(r'^[+-]?\d*\.\d+$', raw_input())))
# TURN TRUE OR FALSE WITH BOOL OPERATION


# Problem2: Re.split()
# It’s guaranteed that every comma and every dot in s is preceeded and followed by a digit.
import re

regex_pattern = "[,.]+"

import re

print("\n".join(re.split(regex_pattern, raw_input())))

# Problem3: Group(), Groups() & Groupdict()
# find the first occurrence of an alphanumeric character in S(read from left to right) that has consecutive repetitions.
import re

match = re.search(r'([a-zA-Z0-9])(\1)', raw_input())

if match:
    print(match.group(1))
else:
    print("-1")

# Problem4: Re.findall() & Re.finditer()
# find all the substrings of string that contains 2 or more vowels.
import re

str = raw_input()  # get string
vowels = 'aeiou'  # seperate vowels and cons
cons = 'qwrtypsdfghjklzxcvbnm'
match = re.findall(r'(?<=[%s])([%s]{2,})[%s]' % (cons, vowels, cons), str,
                   flags=re.I)  # string that contains 2 or more vowels
print('\n'.join(match or ['-1']))

# Problem5: Validating Roman Numerals
# create a regular expression for a valid Roman numeral.
# Output a single line containing True or False according to the instructions above.
regex_pattern = "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
import re

print(str(bool(re.match(regex_pattern, raw_input()))))

# Problem6: Validating phone numbers
import re

num = input()  # number of string
for i in range(0, num):  # take numbers and check first element (789) and len s equal 10 or not
    S = raw_input()
    match = re.search(r'[789][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', S)
    if match and len(S) == 10:
        print('YES')
    else:
        print('NO')

# Problem7: Validating and Parsing Email Addresses
# print each valid email address in the same order as it was received as input.
import re

RE = re.compile(r'^<[a-z][\w.-]+@[a-z]+\.[a-z]{,3}>$', re.I)
n = input()  # number of email address.
for _ in range(n):
    mail = raw_input()  # contains a name and an email address as two space-separated values
    if RE.match(mail.split()[-1]):
        print(mail)

# Problem8: Hex Color Code
#  It must start with a '#' symbol.
# It can have 3 or 6 digits.
# Each digit is in the range of 0 to F
# A-F letters can be lower case
# CHECK THESE
import re

n = input()
out = []

for i in range(n):
    out.extend(re.findall(r'(?<=.)(#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3}?)', raw_input()))
print
'\n'.join(out)

# Problem9: Validating UID
# It must contain at least 2 uppercase English alphabet characters.
# It must contain at least 3 digits (0 - 9).
# It should only contain alphanumeric characters
# No character should repeat.
# There must be exactly 10 characters in a valid UID.
import re

n = input()
for _ in range(n):
    u = ''.join(sorted(raw_input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')

# Problem10: Regex Substitution
# modify those symbols to the following: && → and || → or
import re


def Sub(s):
    s = re.sub(" \&{2} ", " and ", s)
    s = re.sub(" \|{2} ", " or ", s)
    s = re.sub(" \&{2} ", " and ", s)
    return re.sub(" \|{2} ", " or ", s)


n = input()  # take input
for _ in range(n):
    print(Sub(raw_input()))  # take lines

# Problem11: Validating Credit Card Numbers
# It must start with a 4,5 or 6.
# It must contain exactly 16 digits.
# It must only consist of digits (0-9).
# It may have digits in groups of 4, separated by one hyphen "-".
# It must NOT use any other separator like ' ' , '_', etc.
# It must NOT have 4 or more consecutive repeated digits.

import re

n = input()  # number of string
for _ in range(n):
    string = raw_input()
    if not re.match(r'^[456].*', string):
        print('Invalid')
    elif not re.match(r'^\d{16}$|^\d{4}-\d{4}-\d{4}-\d{4}$', string):
        print('Invalid')
    elif not re.match(r'^((\d)(?!\2{3,}))+$', re.sub(r'\D', '', string)):
        print('Invalid')
    else:
        print('Valid')

