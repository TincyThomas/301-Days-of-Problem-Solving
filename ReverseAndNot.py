def reverse_and_not(i):
	n = ""
	for a in str(i):
		n = a+n
	return n+str(i)
print(reverse_and_not(123))
