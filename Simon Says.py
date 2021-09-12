def simon_says(lst1, lst2):
	max1=max(lst1)
	min1=min(lst1)
	max2=max(lst2)
	min2=min(lst2)

	if max2>max1 or min1>min2:
		return True
	else:
		return False
print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))
