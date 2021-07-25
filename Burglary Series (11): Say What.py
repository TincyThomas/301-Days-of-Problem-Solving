def say_what(obj):
	val = ""
	for k,v in obj.items():
		val = val + v +" "
	return val + obj[2]
print(say_what({ 1: "Mommy", 2: "please", 3: "help" }))
