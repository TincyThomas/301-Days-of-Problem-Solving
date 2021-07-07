def mod(a, b):
	div = int(a/b)                   # dividing given inputs
	mul = b * div                    # multiplying one input with quotient
	return a - mul                   # subtracting what we got with what we had to get
print(mod(218, 5))
