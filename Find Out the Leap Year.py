def leap_year(year):
	y = list(year)                                      # taking string to list
	if y[2] == 0 and y[3] == 0:                         # checking last two elements equals 0 or not, it known a year has only 4 elements in it 
		return True if year/400 else False                # leap year is divisible by 400
	else:
		return True if year/4 else False                  # leap year is divisible by 4
print(leap_year(1968))
