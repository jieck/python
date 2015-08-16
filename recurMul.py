a = int(input("a"))
b = int(input('b'))
def recurMul(a,b):
	if b == 1:
		return a
	else:
		return a + recurMul(a,b-1)
recurMul(a,b)
print(recurMul(a,b))