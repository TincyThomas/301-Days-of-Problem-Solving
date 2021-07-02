def match(s1, s2):
	s = s1.upper()                    # making first input string upper 
	t= s2.upper()                     # making second input string upper 
	l = [s]+[t]                       # concatenating to one list
	for i in range(len(s1)):          # looping in the length of any string
		if l[0][i] != l[1][i]:          # checking first element's first equal with second element's first
			return False
	else:
		return True                     # as all are equal return True
print(match("venm", "VENOM"))
