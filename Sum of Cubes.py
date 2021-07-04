def sum_cubes(n):
	a = 0                     # assigning dummy variable equal to zero
	for i in range(n+1):      # looping till n+1
		a = a + i**3            # cube every elements uptil input
	return a
print(sum_cubes(9))
