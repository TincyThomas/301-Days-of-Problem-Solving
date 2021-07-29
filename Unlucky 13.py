def unlucky_13(nums):
	a = []
	for i in nums:
		if i%13!=0:
			a = a + [i]
	return a
print(unlucky_13([53, 182, 435, 591, 637]))
