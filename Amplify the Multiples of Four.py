def amplify(num):
	a = []
	for i in range(1,num+1):
		if i%4 == 0:
			a = a + [i*10]
		else:
			a = a + [i]
	return a
print(amplify(25))
