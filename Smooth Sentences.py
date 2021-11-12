def is_smooth(sentence):
    a = sentence.split(" ")
    for i in a:
        #print(i[len(i) - 1],a[a.index(i) + 1][0])
        if i == a[-2]:
            break
        elif i[len(i) - 1] == a[a.index(i) + 1][0]:
            continue
        else:
            return False
    return True

print(is_smooth("Marta bppreciated deep perpendicular right trapezoids"))
