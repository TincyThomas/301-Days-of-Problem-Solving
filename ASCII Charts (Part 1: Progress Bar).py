def progress_bar(bar, progress):
	a = int(progress//10)
	b = 10-a
	if progress == 100:
		return "|" + str(bar*a) + str(" " *b)+ "| Completed!"
	else: return "|" + str(bar*a) + str(" " *b)+ "| Progress: " + str(progress) + "%"
print(progress_bar("=", 100))
