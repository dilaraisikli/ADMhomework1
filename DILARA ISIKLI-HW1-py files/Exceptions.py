#Exceptions

#Problem1: Exceptions
testcase = input() #number of testcase
for _ in range(testcase):
    valuelist = raw_input().split() #create list and take values into it
    try:
        print int(valuelist[0])/int(valuelist[1]) #try divide
    except ZeroDivisionError as e: #catch the errors with except
        print "Error Code:",e
    except ValueError as e:
        print "Error Code:",e
