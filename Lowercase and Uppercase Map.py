def mapping(letters):
	d = {}
	for i in letters:
		d[i] = i.upper()
	return d
print(mapping(["p", "s"]))
