def compound_interest(p, t, r, n):
	return round(p* (1 + r/n)** (n*t),2)
print(compound_interest(100000, 20, 0.15, 365))
