def day_amount(month, year):
	up = [1,3,5,7,8,10,12]
	down = [4,6,9,11]
	if year%4==0:
		if month ==2:
			return "29"
	else:
		if month in up:
			return "31"
		elif month in down:
			return "30"
		else:
			return "28"
print(day_amount(2, 200))
