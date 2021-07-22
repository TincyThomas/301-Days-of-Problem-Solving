def zip_it(women, men):
	a=[]
	q=[]
	if len(women) == len(men):
		for i in women:
			for j in men:
				a = a+[(i,j)]
		for k in range(0,len(a),len(women)+1):
			q = q+[a[k]]
		return q
	else:
		return "Size does not match"
print(zip_it(["Ana", "Amy", "Lisa"], ["Bob", "Josh", "Tim"]))
