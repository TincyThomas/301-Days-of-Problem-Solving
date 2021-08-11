def check_ending(str1, str2):
    a = ""
    for i in range(-1, -len(str2)-1, -1):
        a = str1[i]+a

    if a == str2:
        return True
    else:
        return False


print(check_ending("abc", "bc"))
