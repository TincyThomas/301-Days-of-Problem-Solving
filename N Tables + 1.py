def n_tables_plus_one(num):
	a = []
	for i in range(1,11):
		a = a+[str((num*i)+1)]
	return ",".join(a)
print(n_tables_plus_one(7))
