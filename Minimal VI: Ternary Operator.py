"""def are_true(a, b):
	if a == True:
		if b == True:
			return "both"
		else:
			return "first"
	elif b = True:
		return "second"
	else:
		return "neither""""
		
		
def are_true(a,b):
	if a == True:
		return "both" if b == True else "First"
	elif b == True:
		return "second"
	else:
		return "neither"
print(are_true(False,False))
