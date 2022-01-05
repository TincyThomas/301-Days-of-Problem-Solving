def concat(*args):
	a = []
	for arg in args:
		for i in arg:
			if type(i)!=int:
				continue
			else:
				a+=[i]
	return a
print(concat(concat([1, 2], [3, 4])))
