def same_ascii(a, b):
    first = 0
    second = 0
    for i in a:
        first = first + ord(i)
    for j in b:
        second = second + ord(j)
    return True if first == second else False


print(same_ascii("EdAbIt", "EDABIT"))
