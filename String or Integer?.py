def int_or_string(var):
	if type(var) == int:                                                  # checking type of input
		return "int"
	if type(var) == str:
		return "str"
print(int_or_string("Welcome to world of programmers!"))
