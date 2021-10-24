def replace_vowel(word):
    d = {"a":1,"e":2,"i":3,"o":4,"u":5}
    l = ["a","e","i","o","u"]
    a = ""
    for i in word:
        if i in l:
            a = a + str(d[i])
        else:
            a = a + i
    return a
print(replace_vowel("karachi"))
