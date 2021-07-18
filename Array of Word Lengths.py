def word_lengths(lst):
    count = 0                                                               # initialization
    a =[]                                                                   # empty list
    for i in lst:                                                           # looping input list
        for j in i:                                                         # looping string 
            count = count + 1                                               # incrementing count
        a = a + [count]                                                     # printing count of each string
        count = 0                                                           # making count 0 after encountering each string
    return a
print(word_lengths(["hola", "people","welcome", "to", "learners", "world" ]))
