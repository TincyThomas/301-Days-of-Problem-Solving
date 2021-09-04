def upward_trend(lst):
	for i in lst:
		if type(i) == str:
			return "Strings not permitted!"
	a = lst
	lst.sort()
	if a == lst:
		return True 
	else:
		return False
print(upward_trend([1, 2, 3, "4"]))
