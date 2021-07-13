def both(n1, n2):
	return True if (n1<0 and n2<0) or (n1>0 and n2>0) or (n1==0 and n2==0) else False         # writing required condition
print(both(1, 5))
