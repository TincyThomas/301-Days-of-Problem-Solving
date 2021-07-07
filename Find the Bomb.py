def bomb(txt):
	l =txt.split(" ")                                         # split using keyword and make it a list
	for i in l:                                               # loop in generated list
		a = i.upper()                                           # make every elements uppercase
		if "BOMB" in a:                                         # now check
			return "Duck!!!"                                      # return subsequent statement
	else:
		return "There is no bomb, relax."
print(bomb("Hey, did you think there is a bomb?"))
