def flick_switch(lst):
    fla = True
    a = []
    for i in lst:
        if i == "flick":
            fla = not fla
        a = a + [fla]
    return a
print(flick_switch([False, False, "flick", "sheep", "flick"]))
