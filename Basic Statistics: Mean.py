def mean(nums):
	a =0                                # initialization
	for i in nums:                      # looping input list
		a = a+i                           # adding values of list
	return round(a/len(nums),1)         # using round() to round by one decimal place
print(mean([1, 3, 8, 9, 9, 10]))
