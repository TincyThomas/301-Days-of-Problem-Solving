def remove_special_characters(txt):
    l = [".", "!","@",  "#" , "$", "%", "^", "&" ,"*", "(", ")" ]
    a = ""
    for i in txt:
        if i not in l:
            a = a + i
    return a


print(remove_special_characters("The quick brown fox!"))
