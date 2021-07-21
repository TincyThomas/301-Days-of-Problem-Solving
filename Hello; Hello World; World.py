def hello_world(num):
	if num%3==0 and num%5==0:
		return "Hello World"
	elif num%5==0:
		return "World"
	elif num%3==0:
		return "Hello"
print(hello_world(3))
