def first_non_repeated_character(txt):
    count = -1
    for i in txt:
        count = count +1
        if txt.count(i)==1:
            return txt[count]
print(first_non_repeated_character("it was then the frothy word met the round night"))
