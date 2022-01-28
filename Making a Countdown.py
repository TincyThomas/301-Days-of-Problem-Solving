def countdown(n, txt):
	a=""
	for i in range(1,n+1):
		a=str(i)+"."+a
	return a+ txt.upper()+"!"
print(countdown(5, "FIRE"))
