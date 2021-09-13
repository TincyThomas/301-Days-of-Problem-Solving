def series_resistance(lst):
	a = 0
	for i in lst:
		a = a + i
	return str(a) + " ohms"
print(series_resistance([1, 5, 6, 3]))
	
