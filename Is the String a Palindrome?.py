def is_palindrome(txt):
	a = ""
	b = ""
	for i in range(int(len(txt)/2)):
		a = a+txt[i]
	for j in range(int(len(txt)/2)+1,len(txt)):
		b = txt[j] + b
	return True if a==b else False
print(is_palindrome("sos"))
