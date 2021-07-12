def find_the_falsehoods(lst):
	a = []
	b = []
	for i in lst:
		if i == 0 or i == () or i== {} or i == [] or i == "" or i == None:
			a = a + [i]
		else:
			i = True
	return a
print(find_the_falsehoods([]))
