def char_count(txt1, txt2):
    count = 0                                   # dummy assignment
    for i in txt2:                              # looping elements of txt2
        if i == txt1:                           # checking when each becomes equal with the text of sentence
            count = count+1                     # increment by 1 everytime
    return count

print(char_count("b", "big fat bubble"))
