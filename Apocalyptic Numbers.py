def apocalyptic(n):
    count = 0
    li = []
    a = str(2 ** n)
    for i in a:
        li = li + [int(i)]
    for j in li:
        count = count + 1
        if j == 6:
            if li[count + 1] == 6:
                if li[count + 1] == 6:
                    return count
            else:
                continue
    else:
        return "Crisis averted. Resume sinning."


print(apocalyptic(157))
	
