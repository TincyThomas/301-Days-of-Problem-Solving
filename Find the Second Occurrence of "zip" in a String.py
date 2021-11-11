def find_zip(txt):
    count = 0
    for i in txt[::-1]:
        count = count + 1
        if i == "z":
            a = txt.index(i)
            if txt[a + 1] == "i":
                if txt[a + 2] == "p":
                    return len(txt)-count
        else:
            return "-1"


print(find_zip("all zip files are compressed"))
