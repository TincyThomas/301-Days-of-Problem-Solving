def can_alternate(s):
    return True if s.count("1") == (s.count("0") - 1) or s.count("1") == (s.count("0") + 1) else False
print(can_alternate("11001"))
