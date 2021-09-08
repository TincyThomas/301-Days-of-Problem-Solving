def showdown(p1, p2):
    count = -1
    cou = -1
    for i in p1:
        count = count + 1
        if i == "B":
            a = count
    for j in p2:
        cou = cou + 1
        if j == "B":
            b = cou
    if a<b:
        return "p1"
    elif a == b:
        return "tie"
    else:
        return "p2"
print(showdown(
  "               Bang! ",
  "             Bang!   "
))
