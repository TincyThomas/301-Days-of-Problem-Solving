def solutions(a, b, c):
	import math
	rot = math.sqrt(b*b - (4 * a *c))
	
	if rot <0:
		return 0
	if rot ==0:
		return 1
	if rot > 0:
		return 2
print(solutions(1, 0, 0) )
