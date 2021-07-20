def second_largest(lst):
	lst.remove(max(lst))
	return max(lst)
print(second_largest([10, 40, 30, 20, 50]))
