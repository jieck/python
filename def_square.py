def square(x):
	return x*x

def twoPower(x,n):
	while n>1:
		x= square(x)
		n = n//2
	return x

x = 4
n = 6
print(twoPower(x,n))