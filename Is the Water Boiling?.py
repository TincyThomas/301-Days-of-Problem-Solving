def is_boiling(temp):
    if temp == "212F" or temp == "100C":
        return True
    else:
        return False


print(is_boiling("10C"))
