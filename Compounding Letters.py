def accum(txt):
	a = ""
	count = 1
	for i in txt.upper():
		a = a + i+ i.lower()*(count-1)
		a = a + "-"
		count = count+1
	return a[:-1]
print(accum("cwAt"))
