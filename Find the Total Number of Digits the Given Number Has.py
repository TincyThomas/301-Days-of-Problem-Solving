def find_digit_amount(num):
	count = 1                             # assigning count variable
	while int(num/10) != 0:               # checking untill ramainder is not equal to 0
		count =count+1                      # with every iteration increment count
		num = int(num/10)                   # change the value of num

	return count


print(find_digit_amount(14255))
	
