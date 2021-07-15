def reverse_capitalize(txt):
    a = ""                              # taking empty string
    for i in txt:                       # looping through input
        a = i.upper() + a               # making every char upper then adding to empty list
    return a
print(reverse_capitalize("abc"))
