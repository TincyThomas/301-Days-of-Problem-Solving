def is_four_letters(lst):
    a = []
    for i in lst:
        if len(i)==4:
            a = a+[i]
    return a

print(is_four_letters(["Tomato", "Potato", "Pair"]))
