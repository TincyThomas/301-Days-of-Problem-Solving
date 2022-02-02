def count(n):
	count=0
	for i in str(n):
		if i.isdigit():
			count +=1
	return count
print(count(-314890))
