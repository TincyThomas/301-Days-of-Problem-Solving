def owofied(sentence):
    count = -1
    sen = list(sentence)
    for i in sen:
        count = count + 1
        if i == "i":
            sen[count] = "wi"
        if i == "e":
            sen[count] = "we"
    return "".join(sen) + " owo"


print(owofied("Cause baby you're a firework"))
