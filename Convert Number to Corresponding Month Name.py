def month_name(num):
	a = {1:'January',2	:'February',3:	'March',4:	'April',5:	'May',6:	'June',7:	'July',8:	'August',9:	'September',10:	'October',11:	'November',12:	'December'}
	for k,v in a.items():
		if num ==k:
			return v
print(month_name(3))
