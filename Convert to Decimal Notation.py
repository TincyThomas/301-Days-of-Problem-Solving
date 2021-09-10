def convert_to_decimal(perc):
	a = []
	for i in perc:
		a = a + [int(i[0:(len(i)-1)])/100]
	return a
print(convert_to_decimal(["1%", "2%", "3%"]))
