def calculate(num1, num2, op):
	a = ""                                    # dummy variable assigning string
	string = num1,op,num2                     # passing inputs to another string variable as atuple
	for i in string:                          # looping tuple
		a = a+str(i)                            # concatenating elements of tuple to string
	return eval(a)                            # eval() works for computation of string expressions
print(calculate(7, 2, "/"))                 # Function calling and printing
