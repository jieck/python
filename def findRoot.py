def findRoot3(x,power,epsilon)
	"""author ccj"""


	if x<0 and power%2 ==0:
		return None
	low = min(-1,x)
	high = max(1,x)
	ans = (high + low)/2.0
	while abs(ans**power-x)>epsilon:
		if ans**power<x:
			low = ans
		else:
			high = ans
		ans = (high + low)/2.0
	return ans
x = input('x = ')
y = input('y = ')
z = input('z = ')
findRoot3(x,y,z)
print(findRoot3(x,y,z))