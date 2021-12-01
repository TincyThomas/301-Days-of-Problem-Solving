def string_pairs(s):
	a = []
	if len(s)%2==0:
		for i in range(0,len(s),2):
			a+=[s[i:i+2]]
		return a
	else:
		s = s+"*"
		for i in range(0,len(s),2):
			a+=[s[i:i+2]]
		return a
print(string_pairs("airforces") )
