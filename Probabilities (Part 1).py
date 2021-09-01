def probability(lst, n):
	count = 0
	for i in lst:
		if i >= n:
			count = count +1
	return round(100*(count/len(lst)),1)
print(probability([7, 4, 17, 14, 12, 3], 16))
