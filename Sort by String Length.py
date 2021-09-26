def sort_by_length(lst):
	d = {}
	key = []
	mai = []
	for i in lst:
		d[len(i)] = i
	for k,v in d.items():
		key = key + [k]
	key.sort()
	for j in key:
		mai = mai + [d[j]]
	return mai
print(sort_by_length(["a", "ccc", "dddd", "bb"]))
