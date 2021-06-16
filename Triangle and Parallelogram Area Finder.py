def area_shape(base, height, shape):
	if shape=="triangle":                                   # check for shape equals to be triangle
		return 0.5*base*height                                # if it is then apply our basic regular triangle formula
	else:
		return base*height                                    # it seems to be a parallelogram, so apply its formula
print(area_shape(8, 6, "parallelogram"))                  # Function calling and checking
