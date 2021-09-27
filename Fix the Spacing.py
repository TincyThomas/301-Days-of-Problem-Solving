def correct_spacing(sentence):
    b = []
    a = sentence.split(" ")
    for i in a:
        if i == "":
            continue
        else:
            b = b + [i]
    return " ".join(b)
print(correct_spacing("The film   starts       at      midnight. "))
