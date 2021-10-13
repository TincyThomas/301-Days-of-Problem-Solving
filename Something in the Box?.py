def in_box(lst):
    for i in lst:
        for j in i:
            if j == "*":
                return True
    else:
        return False


print(in_box([
    "###",
    "#*#",
    "###"
]))
