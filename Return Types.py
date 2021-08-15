def lis_val_type(lst):
	typ = []
	for i in lst:
		if type(i) == int:
			typ = typ + ["int"]
		elif type(i) == str:
			typ = typ + ["str"]
	return typ
print(lis_val_type(["hello", 10]))
