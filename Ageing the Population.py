def after_n_years(names, n):
	a = {}
	for i,j in names.items():
		a[i]=j+n
	return a
print(after_n_years({
  "Joel" : 32,
  "Fred" : 44,
  "Reginald" : 65,
  "Susan" : 33,
  "Julian" : 13
}, 1))
