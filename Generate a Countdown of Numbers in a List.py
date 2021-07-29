def countdown(start):
	a = []
	for i in range(start+1):
		a = [i] + a
	return a
print(countdown(5))
