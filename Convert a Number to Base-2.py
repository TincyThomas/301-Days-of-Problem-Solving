def binary(decimal):
	r  = ''
	while decimal >0:
		rem = decimal % 2
		decimal = int(decimal/2)
		r = r + str(rem)
	return ''.join(r)
print(binary(5))
