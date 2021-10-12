def get_only_evens(nums):
	a = []
	for i in range(0,len(nums),2):
		if nums[i]%2==0:
			a = a + [i]
	return a
print(get_only_evens([1, 2, 3, 4, 5]) )
