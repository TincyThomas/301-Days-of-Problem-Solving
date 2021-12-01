def vol_shell(r1, r2):
	import math
	a = round((4 / 3) * math.pi * ((r1 ** 3) - (r2 ** 3)), 3)
	if a<0:
		return a*(-1)
	else:
		return a


print(vol_shell(3, 800))
