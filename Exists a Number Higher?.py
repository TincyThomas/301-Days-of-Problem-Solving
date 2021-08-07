def exists_higher(lst, n):
	for i in lst:
		if i >=n:
			return True
		else:
			return False
print(exists_higher([4, 3, 3, 3, 2, 2, 2], 7))
