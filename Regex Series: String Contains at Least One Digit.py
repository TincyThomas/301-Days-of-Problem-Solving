def has_digit(txt):
    for i in txt:
        if i.isalpha() == False:
            return True
    else:
        return False
print(has_digit("c"))
