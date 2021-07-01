def is_empty(dictionary):
	for i in dictionary:            # looping elements of given input
		if i != " ":                  # checking equality with empty 
			return False                # if it contains elements then return False
	else:
		return True                   # otherwise True
print(is_empty({ "a": 1 }))
