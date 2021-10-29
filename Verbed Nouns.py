def verbify(txt):
    t = txt.split(" ")
    if t[0][-1]=="e":
        return t[0]+"d "+ t[1]
    elif t[0][-2:]=="ed":
        return txt
    else:
        return t[0]+"ed "+ t[1]
print(verbify("cheesed burger"))
