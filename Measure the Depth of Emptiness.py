def measure_the_depth(lst):
	a = str(lst)                                        # makes input a string
	return int(len(a)/2)                                # we need half of len
print(measure_the_depth([[[[[[[[[[[]]]]]]]]]]]))
