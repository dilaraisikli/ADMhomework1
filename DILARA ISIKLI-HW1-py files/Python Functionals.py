#Python Functionals
#Problem1: Map and Lambda Function
cube = lambda x:x*x*x  #create lambda for cube of x
def fibonacci(n): #create fib. function
    y=0
    z = 1
    for _ in xrange(n):
        yield y  #first of all it should return 0 ,1 and than when n>2 return n**3
        y, z = z, y + z
if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))

