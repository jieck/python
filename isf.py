def isF(s):
	def toChar(s):
		s = s.lower()
		ans = ''
		for c in s:
			if c in "abcdefghijklmnopqrstuvwxyz":
				ans = ans+c
		return ans

	def isFe(s):
		if len(s)<=1:
			return True
		else:
			return s[0]==s[-1] and isFe(s[1:-1])
	return isFe(toChar(s))
s = input('s: ')
print(isF(s))