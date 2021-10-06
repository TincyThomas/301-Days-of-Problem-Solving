def get_discounts(nums, d):
	a  = []
	for i in nums:
		a = a + [(int(d[:-1])/100)*i]
	return a
print(get_discounts([2, 4, 6, 11], "50%"))
