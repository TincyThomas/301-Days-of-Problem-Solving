def sort_by_length(lst):
	d = {}
	a = []
	li = []
	for i in lst:
		d[len(i)] = i
	for k,v in d.items():
		a = a + [k]
	a.sort()
	for j in a:
		li = li + [d[j]]
	return li
print(sort_by_length(["Google", "Apple", "Microsoft"]))
