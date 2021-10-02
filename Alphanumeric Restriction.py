def alphanumeric_restriction(s):
	if s.isalpha() == True:
		return True
	elif s.isdigit() == True:
		return True
	else:
		return False
print(alphanumeric_restriction("85"))
