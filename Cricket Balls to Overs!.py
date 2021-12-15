def total_overs(balls):
	a = str(int(balls/6))
	b = str(balls - (int(balls/6)*6))
	return a+"."+b
print(total_overs(945))
