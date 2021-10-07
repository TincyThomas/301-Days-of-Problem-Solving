def ascii_sort(lst):
	a  = 0
	b = 0
	for j in lst[0]:
		a = a + ord(j)
	for i in lst[1]:
		b= b + ord(i)
	return lst[0] if a < b else lst[1]
print(ascii_sort(["hey", "man"]))
	
		
