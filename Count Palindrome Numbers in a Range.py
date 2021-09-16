def count_palindromes(num1, num2):
	a = []
	w = []
	y = []
	for i in range(num1,num2+1):
		if len(str(i)) == 1:
			a = a + [i]
		else:
			for q in str(i):
				w = w + [q]
			for e in str(i):
				y = [e] + y
			if w == y:
				a = a + [i]
			w = []
			y = []
	return len(a)
print(count_palindromes(878, 898))
