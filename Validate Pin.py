def valid(txt):
    if txt.isdigit():
        if len(txt) == 4 or len(txt) == 6:
            for i in txt:
                if i == " ":
                    return False
                else:
                    return True
        else:
            return False
    else:
        return False


print(valid("12345"))
