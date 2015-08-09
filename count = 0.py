count = 0
sign = 0
s = input('s: ')
while end<=len(s):
    if s[sign:sign+3] == 'bob':
        count+=1
    sign+=1
print('Number of times bob occurs is: '+str(count))