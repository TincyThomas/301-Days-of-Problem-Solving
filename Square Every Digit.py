def square_digits(n):
    a = str(n)
    b = ""
    for i in a:
        b = b + str((int(i)*int(i)))
    return b
print(square_digits(3212))
