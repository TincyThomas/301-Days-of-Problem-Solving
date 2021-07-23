def search(lst, item):
	count = -1
	for i in lst:
		count = count+1
		if i ==item:
			return count
print(search([1, 2, 3, 4], 3))
