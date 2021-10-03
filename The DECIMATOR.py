def DECIMATOR(txt):
    import math
    a = math.ceil(len(txt)/10)
    return txt[:len(txt)-a]
print(DECIMATOR("123456789012345678901"))
