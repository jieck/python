def fac(a):
	if a ==1:
		return a
	else:
		return a*fac(a - 1)
n = int(input('input n : '))
print(fac(n))