def smash_factor(bs, cs):
    a = bs / cs                                             # assigning result of dividing bs by cs
    b = str(a)                                              # converting result to string
    c = b[4]                                                # taking out 3rd element
    d = int(c)                                              # converting 3rd element to int
    e = b[0:4]                                              # taking two digits after point
    f = float(e)                                            # as it is in string now converting it to float
    if d > 5:                                               # checking here whether 3rd element is greater than 5 or not
        return f + 0.01                                     # if it is then add 0.01
    else:
        return f                                            # else print the same


print(smash_factor(154.7, 104.3))
