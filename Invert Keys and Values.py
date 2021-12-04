def invert(dct):
	d = {}
	for k,v in dct.items():
		d[v]=k
	return d
print(invert({ "zebra": "koala", "horse": "camel" }))
