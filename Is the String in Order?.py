def is_in_order(txt):
	a = sort(txt)
	if txt==a:
		return True
	else:
		return False
print(is_in_order("abc"))
