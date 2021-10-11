def valid_str_number(n):
	if n.isdigit() == True:
		return True
	elif n.replace(".","",1).isdigit() == True:
		return True
	else:	return False


print(valid_str_number("324"))
