def format_phone_number(lst):
    a = ""
    for i in lst:
        a = a + str(i)

    return "(" + a[0:3] + ")" +" "+ a[3:6] + "-" + a[6:]
print(format_phone_number([3, 4, 5, 5, 0, 1, 2, 5, 2, 7]))
