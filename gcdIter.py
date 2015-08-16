def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a-b==0:
        return a
    elif a>b:
        return gcdIter(a-b,b)
    else:
        return gcdIter(a,b-a)
a = int(input('a : '))
b = int(input('b : '))
print(gcdIter(a,b))