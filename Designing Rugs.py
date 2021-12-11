def make_rug(m, n, s):
	a = []
	for i in range(m):
		a+= [n*s]
	return a
print(make_rug(2, 2, 'A'))
