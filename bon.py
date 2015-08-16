def bo(n):
	global num
	num+=1
	assert type(n)==int and n>=0
	if n == 0 or n==1:
		return 1
	else:
		return bo(n-1)+bo(n-2)

def testbo(n):
	for i in range(n+1):
		global num
		num = 0
		print('bo of  '+str(i)+' = '+str(bo(i)))
		print('bo called  '+str(num)+' times')
n = int(input('n = '))
testbo(n)