def flip(txt, spec):
	#txt = "There's never enough time to do all the nothing you want"
	a = txt.split(" ")
	b = ""
	n = ""
	q = []
	if spec == "sentence":
		for i in a:
			b = i + " " +b
	return b
print(flip("There's never enough time to do all the nothing you want", "sentence"))
