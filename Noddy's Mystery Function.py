def noddy_function(s):
	if s.upper() == "NODDY":
		return False
	elif s == s.upper():
		return True
	else:
		return False
print(noddy_function("FANTASTIC"))
