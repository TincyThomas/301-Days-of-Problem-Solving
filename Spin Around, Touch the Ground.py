def spin_around(lst):
	a  = 0
	for i in lst:
		if i == "left":
			a= a - 90
		elif i == "right":
			a = a +90

	return int(a/360)
print(spin_around(["right", "right", "right", "right", "right", "right", "right", "right"]))
