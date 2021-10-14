def double_letters(word):
    a = []
    for i in word:
        a = a + [word.count(i)]
    if 2 in a:
        b = a.index(2)
        if a[b+1] == 2:
            return True
        else:
            return False


print(double_letters("oerange"))
