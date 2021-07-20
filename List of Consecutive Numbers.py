def get_sequence(low, high):
	a = []
	for i in range(low,high+1):
		a = a+[i]
	return a
print(get_sequence(98, 100))
