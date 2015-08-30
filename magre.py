def mergeSort(L):
	if len(L) < 2:
		return L[:]
	else:
		left =	mergeSort(L[0:int(len(L)/2)])
		right = mergeSort(L[int(len(L)/2):])

	return merge(left,right)
def merge(left,right):
	i = 0
	j = 0
	result = []
	while(i < len(left) and j < len(right)):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else :
			result.append(right[j])
			j += 1
	while(i < len(left)):
		result.append(left[i])
		i += 1
	while(j < len(right)):
		result.append(right[j])
		j += 1
	return result
L = [10,6,3,2,1,89,3,4,8]
print(mergeSort(L))
