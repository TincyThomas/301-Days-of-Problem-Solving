def to_list(dct):
	a=[]
	for i, j in dct.items():
		a+=[[i,j]]
	return a
print(to_list({ "shrimp": 15, "tots": 12 }))
