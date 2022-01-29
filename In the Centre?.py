def is_central(txt):
    a = len(txt)
    count = 0
    for i in txt:
        count += 1
        if i != " ":
            ind = count
    if a%2==0:
        return False
    else:
        return True if ind == int(a / 2) + 1 else False


print(is_central(" @"))
