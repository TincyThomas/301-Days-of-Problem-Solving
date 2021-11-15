def find_occurrences(txt, ch):
	d = {}
	a = txt.split(" ")
	for i in a:
		d[i]=i.count(ch)
	return d
print(find_occurrences("Hello World", "o"))
