# Paste your code into this box 
s = input('input s : ')
str1 = s[0]
strTemp = s[0]
first = 0
intor = 0
while intor < (len(s)-1):
    if s[intor+1]>=s[intor]:
        strTemp =s[first:intor+2]
        print(strTemp)
    else:
    	first=intor+1
    if len(str1)<len(strTemp):
        str1 = strTemp
    intor+=1
print('Longest substring in alphabetical order is: '+str1)