def is_anagram(s1, s2):
	a = set(s1.lower())
	b= set(s2.lower())
	if a == b:
		return True
	else:
		return False
print(is_anagram("cristian", "Cristina"))
	
