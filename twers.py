def printMove(fr,to):
	print('move from '+str(fr)+'   to   '+ to )

def Towers(n,fr,to,spare):
	if n == 1:
		printMove(fr,to)
	else:
		Towers(n-1,fr,spare,to)
		Towers(1,fr,to,spare)
		Towers(n-1,spare,to,fr)

n=10
fr = 'fr'
to = 'to'
spare = 'spare'
Towers(n,'1','2','3')