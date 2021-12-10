def unique_in_order(sequence):
	lis = sequence[0]
	for i in range(1,len(sequence)):
		if sequence[i-1]==sequence[i]:
			lis+=""
		else:
			lis+=sequence[i]
	return list(lis)
print(unique_in_order("ABBCcAD"))
