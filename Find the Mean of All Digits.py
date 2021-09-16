def mean(num):
	b = 0
	a = str(num)
	for i in a:
		b = b + int(i)
	return int(b/len(a))
print(mean(12345))
