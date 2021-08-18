def running_athlete(act, txt):
    count = -1
    a = []
    for i in act:
        count = count + 1
        if i == 'run':
            if txt[count] != "_":
                a = a + ["/"]
            else:
                a = a +["_"]
        elif i == 'jump':
            if txt[count] != "|":
                a = a + ["x"]
            else:
                a = a + ["|"]
    return ''.join(a)


print(running_athlete(["run", "jump", "run", "run", "run"], "_|_|_"))

