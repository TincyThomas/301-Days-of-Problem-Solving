def alliteration_correct(sentence):
    a = []
    s = sentence.split()
    for i in s:
        print(i)
        if len(i) >= 4:
            a = a + [i[0]]
    return True if len(set(a)) == 1 else False


print(alliteration_correct("She swam to the phore."))
