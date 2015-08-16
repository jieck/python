def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a%b==0:
        return b
    else:
        return gcdIter(b,a%b)
a = int(input('a : '))
b = int(input('b : '))
print(gcdIter(a,b))