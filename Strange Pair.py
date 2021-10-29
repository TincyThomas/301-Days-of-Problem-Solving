def is_strange_pair(txt1, txt2):
    return True if txt1[0] == txt2[-1] and txt1[-1] == txt2[0] else False


print(is_strange_pair("bush", "hubris"))
