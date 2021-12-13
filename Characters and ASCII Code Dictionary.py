def to_dict(lst):
	d = {}
	for i in lst:
		d[i]= ord(i)
	return [d]
print(to_dict(["a", "b", "c"]))
