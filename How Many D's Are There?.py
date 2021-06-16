def count_d(sentence):  
    a = sentence.lower()                                                # converting sentence to lowercase, you can to upper if you want
    return a.count("d")                                                 # counting "d" in sentence which is currently stored in variable a

print(count_d("Debris was scattered all over the yard."))               # function calling and printing
