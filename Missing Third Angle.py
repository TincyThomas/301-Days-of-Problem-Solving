def missing_angle(angle1, angle2):
	a = 180 - (angle1 + angle2)
	if a < 90:
		return "acute"
	elif a ==90:
		return "right"
	else:
		return "obtuse"
print(missing_angle(27, 59))
