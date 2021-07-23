def arithmetic_progression(start, diff, n):
	a = [str(start)]
	for i in range(1,n):
		start = start + diff
		a.append(str(start))
	return ",".join(a)
print(arithmetic_progression(1, 2, 5))
