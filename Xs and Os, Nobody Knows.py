def XO(txt):
    t = txt.upper()
    a = t.count("X")
    b = t.count("O")
    return True if a == b else False


print(XO("ooXm"))
-
