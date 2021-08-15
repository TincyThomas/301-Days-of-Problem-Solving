def sum_common(lst1, lst2, lst3):
	a = []
	b = []
	z = 0
	for i in lst1:
		for j in lst2:
			if i == j:
				a = a+[i]
	for k in a:
		for l in lst3:
			if k == l:
				b = b+[k]
	for q in b:
		z = z+q
	return z
print(sum_common([1], [1], [2]) )
