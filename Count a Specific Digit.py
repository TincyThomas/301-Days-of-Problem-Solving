def digit_occurrences(start, end, digit):
	a=""
	count=0
	for i in range(start,end+1):
		a+=str(i)
	for j in a:
		if j == "-":
			continue
		if int(j)==digit:
			count+=1
	return count
print(digit_occurrences(-8, -1, 8))
