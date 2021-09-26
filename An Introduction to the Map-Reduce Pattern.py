def magnitude(lst):
	a = 0
	for i in lst:
		a = a + (i**2)
	return (a)**(1/2)
print(magnitude([2, 3, 6, 1, 8] ))
