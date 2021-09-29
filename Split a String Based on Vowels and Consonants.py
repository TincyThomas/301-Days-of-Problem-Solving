def split(txt):
    b = ""
    c = ""
    a = ["a","e","i","o","u"]
    for i in txt:
        if i in a:
            b= b+i
        else:
            c= c + i
    return b+c
print(split("What's the time?"))
