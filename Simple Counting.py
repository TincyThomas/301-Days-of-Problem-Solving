def count_digits(n, d):
	a = ""
	for i in range(1,n+1):
		a = a+str(i*i)
	return a.count(str(d))
print(count_digits(25, 2))
