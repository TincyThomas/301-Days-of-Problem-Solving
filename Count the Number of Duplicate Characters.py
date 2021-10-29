def duplicate_count(txt):
    a = []
    count = 0
    for i in txt:
        a = a + [txt.count(i)]
        txt = txt.replace(i,"")
    for i in a:
        if i >1:
            count = count +1
    return count
print(duplicate_count("Indivisibilities"))
