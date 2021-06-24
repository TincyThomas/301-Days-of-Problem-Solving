def weight_allowed(car, p, max_weight):
	w = (1/ 0.453592) * max_weight                                        # think, this is conversion formula
	sum = 0                                                               # dummy assignment
	for i in p:                                                           # p is a list
		sum = sum + i                                                       # adding elements of p
	main = car + sum                                                      # adding car's and passenger's weight
	if main < w:                                                          # check
		return True
	else:
		return False
print(weight_allowed(3000, [150, 201, 75, 88, 195], 1700))
