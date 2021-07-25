def free_shipping(order):
	a = 0
	for k, v in order.items():
		a = a+v
	if a>50.00:
		return True
	else:
		return False
print(free_shipping({ "Shampoo": 15.99, "Rubber Ducks": 15.99 }))
