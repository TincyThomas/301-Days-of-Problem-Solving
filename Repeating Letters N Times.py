def repeat(txt, n):
	a = ""
	for i in txt:
		a = a+ (i*n)
	return a
print(repeat("mice", 5))
