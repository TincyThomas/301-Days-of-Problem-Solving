def quadratic_equation(a, b, c):
	import math
	rot = math.sqrt(b*b - (4 * a *c))
	return (-b+ (rot)) /(2*a)
print(quadratic_equation(2, -7, 3))
