def count_syllables(txt):
    t = txt.upper()                         # making uppercase
    a = t[0] + t[1]                         # taking first two char
    return t.count(a)                       # print count of a in txt


print(count_syllables("hehehehehehe"))
