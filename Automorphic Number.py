def automorphic(n):
	return True if (n*n)%10 == n else False             # n*n is square... doing mod 10 returns last digit
print(automorphic(3))
