def bbq_skewers(grill):
	veg = 0
	nonveg = 0
	for i in grill:
		if "x" in i:
			nonveg = nonveg +1
		elif "o" in i:
			veg = veg +1
	return [veg, nonveg]
print(bbq_skewers([
  "--oooo-ooo--",
  "--xx--x--xx--",
  "--o---o--oo--",
  "--xx--x--ox--",
  "--xx--x--ox--"
]))
