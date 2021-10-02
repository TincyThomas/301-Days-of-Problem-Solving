def factor_chain(lst):
	count = 0
	for i in range(1,len(lst)):
		if lst[i]%lst[i-1]==0:
			continue
		else:
			return False
	return True
print(factor_chain([1, 2, 4, 8, 16, 32]))
		
