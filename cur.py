def cur(n,from , to , sqare):
	if n = 1 :
		print(str(from)+'  to  '+str(to))
	else:
		cur(n-1, from , sqare , to)
		cur(1, from , to , sqare)
		cur(n-1, sqare , to , from)
