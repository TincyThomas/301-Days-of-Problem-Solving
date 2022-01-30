def match_last_item(lst):
    a = ""
    for i in lst[:len(lst)-1]:
        a+=str(i)
    return True if a == lst[-1] else False
print(match_last_item([1, 1, 1, "11"]))
