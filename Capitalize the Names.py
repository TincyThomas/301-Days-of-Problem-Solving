def cap_me(lst):
	a = []
	for i in lst:
		a = a+[i[0].upper()+i[1:]]
	return a
print(cap_me(["mavis", "senaida", "letty"]))
