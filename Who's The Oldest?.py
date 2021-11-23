def oldest(people):
	count = -1
	a = []
	b = []
	for k,v in people.items():
		count +=1
		a = a + [v]
		b +=[k]
		c = max(a)
		d = a.index(c)
	return b[d]

print(oldest({"Emma": 71,"Jack": 45,"Amy": 15,"Ben": 29}))
