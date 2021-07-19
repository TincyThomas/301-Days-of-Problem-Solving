def operation(num1, num2):
	if num1+num2==24:
		return "added"
	elif num1*num2==24:
		return "multiplied"
	elif num1/num2==24:
		return "divided"
	elif num1-num2==24:
		return "subtracted"
	else:
		return "None"
print(operation(22, 2))
