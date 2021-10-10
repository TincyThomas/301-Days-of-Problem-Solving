def longest_zero(s):
	a = s.split("1")
	l = []
	d = {}
	for j in a:
		l = l + [len(j)]
		d[len(j)] = j
	for k,v in d.items():
		if k == max(l):
			return v
print(longest_zero("111"))
