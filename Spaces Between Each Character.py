def space_me_out(s):
    a = ""                                      # empty string
    for i in s:                                 # looping through input
        a = a + i + " "                         # adding each element with a space in between
    return a

print(space_me_out("welcome to space"))
