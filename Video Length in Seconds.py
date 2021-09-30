def minutes_to_seconds(time):
	a = time[0:2]
	c = time[3:5]
	return (int(a)*60) + int(c)
print(minutes_to_seconds("13:56"))
