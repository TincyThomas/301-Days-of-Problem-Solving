def get_type(value):
	a = str(type(value))
	return a[8:len(a)-2]
print(get_type("abdc"))
