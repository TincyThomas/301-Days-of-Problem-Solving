def cars_needed(n):
	if n%5==0:
		return int(n/5)
	else:
		return int(n/5)+1
print(cars_needed(1))
