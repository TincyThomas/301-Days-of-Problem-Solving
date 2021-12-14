import math
def line_length(dot1, dot2):
	return round(math.sqrt((dot1[0]-dot2[0])**2+(dot1[1]-dot2[1])**2),2)
print(line_length([15, 7], [22, 11]))
