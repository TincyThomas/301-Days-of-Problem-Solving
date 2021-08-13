def increment_to_top(lst):
	a = max(lst)
	q = 0
	for i in lst:
		q = q + (a-i)
	return q
print(increment_to_top([4, 3, 4]))
