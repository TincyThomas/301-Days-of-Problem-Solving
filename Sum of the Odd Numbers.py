def add_odd_to_n(n):
	a = 0
	for i in range(n+1):
		if i%2!=0:
			a = a+i
	return a
print(add_odd_to_n(47))
