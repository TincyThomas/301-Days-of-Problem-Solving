def missing_num(lst):
	a = []
	for i in range(1,11):
		a = a+[i]
	for j in a:
			if j in lst:
				continue
			else:
				return j
print(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]))
