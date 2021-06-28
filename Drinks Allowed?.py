def should_serve_drinks(age, on_break):
	return True if (age>=18) and on_break == False else False                 # check on age and whether they are on break or not
print(should_serve_drinks(30, True))
