def reverse_list(num):
	b = str(num)
	a = []
	for i in b:
		a = [int(i)] + a
	return a
print(reverse_list(1485979))
