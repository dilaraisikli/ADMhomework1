# Date and Time
# Problem1: Calendar Module
# find what the day is on that date.
import datetime
from datetime import date
import calendar

day = map(int, raw_input().split())  # take a day
DateofDay = datetime.date(day[2], day[0], day[1])
result = DateofDay.strftime("%A")
resultUpper = result.upper()  # make upper string for true result.
print
resultUpper

# Problem2: Time Delta
import datetime as dt

MonthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']  # create month list


def Month(month):  # turn month to integer value

    for index, item in enumerate(MonthList):
        if month == item:
            return index + 1


def CalMin(zone):  # turn poz
    neg = False
    if (zone < 0):
        neg = True
        zone = - zone
    hr = zone / 100
    mins = zone % 100
    value = hr * 60 + mins
    if neg:
        value = - value  # turn poz
    return dt.timedelta(minutes=value)


def CalDT(_str):  # take date and fit it "datetime"
    split = _str.split(' ')
    time = [int(x) for x in split[4].split(':')]
    dd = int(split[1])
    mm = Month(split[2])
    yyyy = int(split[3])
    result = dt.datetime(yyyy, mm, dd, time[0], time[1], time[2])
    tz = int(split[5])
    delta = CalMin(tz)
    return result - delta


def CalSec(td):
    return td.days * 86400 + td.seconds


N = int(raw_input())
for i in range(N):
    dt1 = CalDT(raw_input())
    dt2 = CalDT(raw_input())
    print
    abs(CalSec(dt1 - dt2))


