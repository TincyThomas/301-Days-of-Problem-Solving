def fib(n):
	a = [0,1]
	s = 1
	count = 0
	while count<n-1:
		a = a + [a[count]+a[count+1]]
		count = count + 1
	return a[n]
print(fib(2))
