def multiply(l):
	b = []
	a = len(l)
	for i in l:
		b += [[i]*a]
	return b
print(multiply([4,2, 5]))
