def is_curzon(num):
	if (2 ** num + 1) % (2 * num + 1) == 0:
		return str(2 ** num + 1)+ str(" is a multiple of ") + str(2 * num + 1)
	else:
		return str(2 ** num + 1)+ str(" is not a multiple of ") + str(2 * num + 1)
print(is_curzon(10))
