def sum_found_indexes(lst, n):
	count = -1
	a = 0
	for i in lst:
		count = count+1
		if i == n:
			a = a+count
	return a
print(sum_found_indexes([0, 3, 3, 0, 0, 3], 3))
		
