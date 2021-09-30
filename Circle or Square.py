def circle_or_square(rad, area):
	return True if ((22/7)*2*rad)> (4* (area)**(1/2)) else False
print(circle_or_square(5, 100))
