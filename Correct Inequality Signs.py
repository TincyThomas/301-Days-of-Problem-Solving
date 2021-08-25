def correct_signs(txt):
    count = 0
    a = txt.split()
    for i in a:
        if i == "<" or i == ">":
            count = count +1
    for i in range(0,count+1,2):
        if int(a[i]) < int(a[i+2]):
            if a[i+1] == "<":
                continue
        else:  return False
    return True


print(correct_signs("13 > 44 > 33 > 1"))
