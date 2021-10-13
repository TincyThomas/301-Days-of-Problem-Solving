# "a"s with 4, "e"s with 3, "i"s with 1, "o"s with 0, and "s"s with 5.
def hacker_speak(txt):
    count  = -1
    a = ""
    for i in txt:
        count = count +1
        if i == "a":
            a = a + ("4")
        elif i == "e":
            a = a + ("3")
        elif i == "i":
            a = a + ("1")
        elif i == "o":
            a = a + ("0")
        elif i == "s":
            a = a + ("5")
        else:
            a = a + i
    return a
print(hacker_speak("become a coder"))
