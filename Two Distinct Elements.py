def return_unique(lst):
	a = []
	for i in lst:
		if lst.count(i)>1:
			continue
		else:
			a +=[i]
	return a
print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))
