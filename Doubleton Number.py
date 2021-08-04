def doubleton(n):
	start = n
	end=n+1
	while(True):
		for i in range(start,end):
			a = str(i)
			b = list(a)
			c= set(b)
			if len(c) == 2:
				return i
			else:
				end = end+1
print(doubleton(10))

	
