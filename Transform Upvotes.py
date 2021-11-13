def transform_upvotes(txt):
	a = txt.split(" ")
	q = []
	count = -1
	n = []
	for i in a:
		if i[-1]=="k":
			n = n+ [i[:-1]+"000"]
		else:
			n = n + [i]
	for j in n:
		for k in j:
			count = count +1
			if k == ".":
				q = q + [j[:count]+j[count+1:-1]]
		count = -1
	else:
		q = q + [j]

	return q
print(transform_upvotes("20.3k 3.8k 7.7k 992"))
