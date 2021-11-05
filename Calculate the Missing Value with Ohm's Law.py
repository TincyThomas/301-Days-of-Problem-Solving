def ohms_law(v, r, i):
	if v == None:
		return round(r*i,2)
	elif r == None:
		return round(v/i,2)
	else:
		return round(v/r,2)
print(ohms_law(12, 220, None))
