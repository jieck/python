def newSort(L):
	for i in range(len(L) - 1):
		j = i+1
		while j<len(L):
			if L[i] > L[j]:
				temp = L[i]
				L[i] = L[j]
				L[j] = temp
			j +=1
L = [10 , 9, 8, 5, 3]
newSort(L)
print(L)
