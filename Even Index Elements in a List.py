def even_last(lst):
	a = ""
	for i in range(len(lst) + 1):
		if i % 2 == 0:
			a = a + str(lst[i])
			z = a
			a = a+ "+"
	return eval(z)*lst[-1]

print(even_last([-11, 3, 3, 1, 10]))
