def is_truthy(val):
	return 0 if val == False or val == None or val ==0 or val == [] or val == {} or val =="" else 1
print(is_truthy(False))
