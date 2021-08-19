def mood_today(mood):
	if mood == "":
		return "Today, I am feeling neutral"
	else:
		return "Today, I am feeling " + mood
print(mood_today(""))
