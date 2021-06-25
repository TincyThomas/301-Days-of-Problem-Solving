def check_equals(lst1, lst2):
	if (lst1[::] == lst2[::]):                            # checking whether two list equal or not
		return True
	else:
		return False

print(check_equals([11, 2], [11, 2]))
