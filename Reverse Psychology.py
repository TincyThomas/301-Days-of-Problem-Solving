def reverse_psychology(s):
    a = "Do not "                                             # do as question says
    if a in s:
        return s[7:len(s)]
    else:
        return "Do not " + s[:]
print(reverse_psychology("Do not wash the dishes"))
