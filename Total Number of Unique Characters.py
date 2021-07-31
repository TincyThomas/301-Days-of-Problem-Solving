def count_unique(s1, s2):
	a = []
	for i in s1:
		a = a+[i]
	for j in s2:
		a = a+[j]
	return len(set(a))
print(count_unique("sore", "zebra"))
