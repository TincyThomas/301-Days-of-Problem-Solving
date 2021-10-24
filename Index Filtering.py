def index_filter(indexes, string):
	a = ""
	for i in indexes:
		a = a + string[i]
	return a
print(index_filter([2, 3, 8, 11], "Autumn in New York"))
