def list_between(num1, num2, lst):
	a = []
	for i in range(num1+1,num2):
		for j in lst:
			if i == j:
				a = a +[i]
	return a
print(list_between(3, 8, [3, 5, 95, 0, 4, 7]))
