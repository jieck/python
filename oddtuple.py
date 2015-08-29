def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    x = aTup
    x1 = ()
    for x in range(len(aTup)):
        if x == len(aTup)-1 or aTup[x][0]!=aTup[x+1][0]:
            x1= x1 + (aTup[x],)
    print(x1)
aTup=('aadd','cba','cef')
oddTuples(aTup)