def printMove(fr,to):
	print('move from '+str(fr)+'   to   '+str(to))
	
def Towers(n,fr,to,spare):
	if n==1:
		printMove(fr,to)
	else:
		Towers(n-1,fr,spare,to)
		Towers(1,fr,to,spare)
		Towers(n-1,spare,to,fr)
n = 5
fr = '1'
to = '2'
spare = '3'
Towers(n,fr,to,spare)