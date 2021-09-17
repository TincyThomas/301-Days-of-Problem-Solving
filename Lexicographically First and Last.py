def first_and_last(s):
	a = []
	b = []
	for i in s:
		a = a + [i]
	a.sort()
	for j in a:
		b = [j] + b
	a = "".join(a)
	b = "".join(b)
	return [a,b]
print(first_and_last("marmite"))
