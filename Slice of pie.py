def equal_slices(total, people, each):
	a = people * each                             # people multiplied by each gives amount of required slices stored in a variable
	return True if a<=total else False            # check if computed values is less than total return true if 
print(equal_slices(8, 3, 2))
