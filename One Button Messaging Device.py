def how_many_times(msg):
	import string
	count = 1
	sum = 0
	d = {}
	al = string. ascii_lowercase
	al = list(al)
	for i in al:
		d[i] = count
		count = count+1
	for k,v in d.items():
		for j in msg:
			if j == k:
				sum =sum +v
	return sum
print(how_many_times("abde"))
