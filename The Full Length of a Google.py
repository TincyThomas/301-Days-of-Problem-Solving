def googlify(n):
	if n<0:                             # pre telling if n is less then it is invalid
		return "Invalid Input"
	return "G" + n*"o" * "gle"          # otherwise concatenating n number of o's
print(googlify(2))
