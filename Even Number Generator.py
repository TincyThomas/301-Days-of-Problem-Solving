def find_even_nums(num):
	a = []
	for i in range(1,num+1):
		if i%2==0:
			a = a + [i]
	return a
print(find_even_nums(8))
