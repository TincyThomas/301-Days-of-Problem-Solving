
# question hint
'''def increment_items(lst)
	for i in list:
		i += 1
	return list''''


# Answer 
def increment_items(list):
	a = []
	for i in list:
		i = i + 1
		a =a + [i]
	return a
print(increment_items([-1, -2, -3, -4]))
