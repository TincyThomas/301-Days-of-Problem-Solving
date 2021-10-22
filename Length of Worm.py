def worm_length(worm):
	for i in worm:
		if i!="-":
			return "Invalid"
		else:
			continue
	return str(len(worm)*10) + " mm"
print(worm_length("--_--------"))
