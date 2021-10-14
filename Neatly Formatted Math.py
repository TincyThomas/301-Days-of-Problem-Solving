def format_math(expr):
	if "X" in expr:
		a = expr.replace('X','*')
	return expr + " = " + str(int(eval(a)))
print(format_math("6 X 3"))
