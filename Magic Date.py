def magic(txt):
    t = txt.split(" ")
    print(t)
    if len(str(int(t[0])*int(t[1])))== 1:
        if int(t[2][-1]) == int(t[0])*int(t[1]):
            return True
    if len(str(int(t[0])*int(t[1])))== 2:
        if int(t[2][-2:]) == int(t[0])*int(t[1]):
            return True
    if len(str(int(t[0])*int(t[1])))== 3:
        if int(t[2][-3:]) == int(t[0])*int(t[1]):
            return True
print(magic("10 10 2100"))
