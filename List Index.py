def list_index(lst, idx):
	count = 0
	a = ""
	for i in lst:
		for k in i:
			count = count +1
			for j in idx:
				if j == count:
					a = a+ k
	return a
print(list_index([["m", "u", "b"],["a", "s", "h"],["i", "r", "1"]], [1, 3, 5, 8]))
