def is_good_match(lst):
	a = []
	if len(lst) %2 !=0:
		return "bad match"
	else:
		for i in range(0,len(lst),2):
			a = a + [lst[i] + lst[i+1]]
	return a
print(is_good_match([5, 7, 9, -1, 4, 2]))
