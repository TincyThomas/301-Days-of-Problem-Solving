def unique(lst):
	li = []
	d = {}
	s = set(lst)
	for i in s:
		d[i] = lst.count(i)
	for k,v in d.items():
		li = li + [v]
	mi = min(li)
	for k, v in d.items():
		if v == mi:
			return k
print(unique([3, 3, 3, 7, 3, 3]))
