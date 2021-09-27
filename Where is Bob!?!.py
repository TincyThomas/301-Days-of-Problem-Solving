def find_bob(names):
	if "Bob" not in names:
		return -1
	else:
		return names.index("Bob")
print(find_bob(["Jimmy", "Layla", "James","Bob"]))
