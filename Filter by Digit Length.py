def filter_digit_length(lst, num):
	a= []
	for i in lst:
		if len(str(i))==num:
			a = a+ [i]
	return a
print(filter_digit_length([88, 232, 4, 9721, 555], 4))
