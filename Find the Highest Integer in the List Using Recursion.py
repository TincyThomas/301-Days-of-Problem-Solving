def find_highest(lst):
	a = 0
	count  = -1
	for i in lst:
		count+=1
		if i>=a:
			a = i
		else:
			find_highest(lst[count+1:])
	return a
print(find_highest([0, 12, 4, 87, 6]))
