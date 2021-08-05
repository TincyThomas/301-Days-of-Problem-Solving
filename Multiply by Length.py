def MultiplyByLength(arr):
	a = []
	for i in arr:
		a = a+[i*len(arr)]
	return a
print(MultiplyByLength([2, 3, 1, 0]))
