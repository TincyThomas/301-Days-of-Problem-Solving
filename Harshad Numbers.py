def is_harshad(num):
	a=0
	n =str(num)
	for i in n:
		a = a + int(i)
	return True if num%a ==0 else False
print(is_harshad(41))
