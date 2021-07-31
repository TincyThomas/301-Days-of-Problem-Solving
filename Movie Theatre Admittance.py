def accept_into_movie(age, is_supervised):
	if age>=15 or is_supervised == True:
		return True
	else:
		return False
print(accept_into_movie(14, True))
