def md_format(word, style):
	if style == "b":
		return "**"+word+"**"
	elif style=="i":
		return "_"+word+"_"
	elif style=="c":
		return "`"+word+"`"
	elif style == "s":
		return "~~"+word+"~~"
print(md_format("leaning text", "i"))
