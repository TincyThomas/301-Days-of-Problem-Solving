def collatz(num):
	count = 0
	while True:
		count = count +1
		if num%2==0:
			num = num / 2
			if num==1:
			    return count
		else:
		    num = num * 3 + 1
		    if num==1:
			    return count
print(collatz(2))
