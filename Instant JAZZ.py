def jazzify(lst):
	a = []
	for i in lst:
		a = a + [i+"7"]
	return a
print(jazzify(["G", "F", "C"]))
