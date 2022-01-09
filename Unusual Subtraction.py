def not_good_math(n, k):
	a =0
	b = str(n)
	if b[-1]=="0":
		n = b[:-1]
		n = int(n)
		k = k-1

	for i in range(k):
		a = n -1
		n = a
	return a
print(not_good_math(540, 5))
