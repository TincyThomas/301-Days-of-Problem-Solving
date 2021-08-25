def evenly_divisible(a, b, c):
	q = 0
	for i in range(a,b+1):
		if i %c==0:
			q = q +i
		else: continue
	return q
print(evenly_divisible(1, 10, 2))
