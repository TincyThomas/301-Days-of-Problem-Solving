def findLargestNums(lst):
	a = []
	for i in lst:
		a= a+[max(i)]
	return a
print(findLargestNums([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]]))
