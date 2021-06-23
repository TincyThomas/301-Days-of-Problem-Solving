def distance_home(lst):
	a = 0                                                   # dummy assignment 
	for i in lst:                                           # looping elements of lst
		a = a+i                                               # adding i to its previous sum
	return a                                                # return last sum
print(distance_home([3, 5, -5, -2]))                      # function calling and prinitng
