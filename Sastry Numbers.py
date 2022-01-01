def is_sastry(n):
    a = n + 1
    b = str(n) + str(a)
    return True if int(b) ** (1 / 2) == int(int(b) ** (1 / 2)) else False

print(is_sastry(183))

