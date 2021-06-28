def keyboard_mistakes(txt):
    s = list(txt)                             # converting txt to list
    for i in txt:                             # looping txt
        if i == "5":
            a = txt.index(i)                  # taking index of 5
            s[a] = "S"                        # placing S at that index
        elif i == "1":
            a = txt.index(i)                  # taking index of 1
            s[a] = "I"                        # placing I at that index
        elif i == "4":
            a = txt.index(i)                  # taking index of 4
            s[a] = "A"                        # placing A at that index
        elif i == "0":
            a = txt.index(i)                  # taking index of 0
            s[a] = "O"                        # placing O at that index
    return ''.join(s)                         # at last return in a string format concatenating spaces

print(keyboard_mistakes("51NG4P0RE"))         # Function calling and printing
