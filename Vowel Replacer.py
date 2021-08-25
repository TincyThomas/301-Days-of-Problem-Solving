def replace_vowels(txt, ch):
    count = -1
    a =""
    for i in txt:
        count = count +1
        if i =="a" or i =="e"or i =="o"or i =="u" or i =="i":
            a= a+ch
        else:
            a= a+txt[count]
    return a
print(replace_vowels("the aardvark", "#"))
