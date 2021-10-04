def get_frequencies(lst):
	d = {}
	l = set(lst)
	for i in l:
		d[i]= lst.count(i)
	return d
print(get_frequencies([True, False, True, False, False]))
