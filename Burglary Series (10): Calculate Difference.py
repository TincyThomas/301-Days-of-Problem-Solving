def calc_diff(obj, limit):
	a = 0
	for k,v in obj.items():
		a = a + v
	return a -limit
print(calc_diff({ "baseball bat": 20 }, 5))
