def letter_check(lst):
    for i in lst[1]:
        if i in lst[0]:
            continue
        else:
            return False
    else:
        return True


print(letter_check(["parses", "parsecs"]))
