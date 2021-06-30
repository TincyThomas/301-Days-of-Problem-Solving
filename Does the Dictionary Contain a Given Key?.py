def has_key(dictionary, key):
	for keys in dictionary:                                       # looping keys of dictionary
		if keys == key:                                             # checking whether looped key equals to input
			return True                                               # if it is then true
		else:
			continue                                                  # continue is here to execute until end
	return False                                                  # otherwise
print(has_key({ "pot": 1, "tot": 2, "not": 3 }, "kia"))
